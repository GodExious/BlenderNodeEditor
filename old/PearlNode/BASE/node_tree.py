import bpy
import uuid

from bpy.types import NodeTree

from .runtime import cache_node_dependants, \
    cache_socket_links, \
    cache_node_group_outputs, \
    cache_executed_nodes, \
    cache_socket_variables, \
    runtime_info, \
    logger

class NodeTreeBase(bpy.types.NodeTree):
    def get_other_socket(self, socket):
        '''
        Returns connected socket

        It takes O(len(nodetree.links)) time to iterate thought the links to check the connected socket
        To avoid doing the look up every time, the connections are cached in a dictionary
        The dictionary is emptied whenever a socket/connection/node changes in the nodetree
        '''
        # accessing links Takes O(len(nodetree.links)) time.
        _nodetree_socket_connections = cache_socket_links.setdefault(self, {})
        _connected_socket = _nodetree_socket_connections.get(socket, None)

        if _connected_socket:
            return _connected_socket

        socket = socket
        if socket.is_output:
            while socket.links and socket.links[0].to_node.bl_rna.name == 'Reroute':
                socket = socket.links[0].to_node.outputs[0]
            if socket.links:
                _connected_socket = socket.links[0].to_socket
        else:
            while socket.links and socket.links[0].from_node.bl_rna.name == 'Reroute':
                socket = socket.links[0].from_node.inputs[0]
            if socket.links:
                _connected_socket = socket.links[0].from_socket

        cache_socket_links[self][socket] = _connected_socket
        return _connected_socket

    def update(self):
        '''Called when the nodetree sockets or links change, socket pair cache is cleared here'''
        if not runtime_info['executing']:
            if self in cache_socket_links:
                del cache_socket_links[self]
            if self in cache_node_group_outputs:
                del cache_node_group_outputs[self]
            # if self in cache_tree_portals:
            #     del cache_tree_portals[self]
            if self in cache_node_dependants:
                del cache_node_dependants[self]
        else:
            print('TRIED TO UPDATE TREE, BUT ITS EXECUTING')
        # change the socket of the reroute nodes
        for node in self.nodes:
            if node.bl_idname == 'NodeReroute':
                connected = self.get_other_socket(node.inputs[0])
                if connected and connected.bl_idname != node.inputs[
                    0].bl_idname:
                    new_input = node.inputs.new(connected.bl_idname, '')
                    # new_input.init_from_socket(connected.node, connected)
                    new_output = node.outputs.new(connected.bl_idname, '')
                    # new_output.init_from_socket(connected.node, connected)
                    self.relink_socket(node.inputs[0], new_input)
                    self.relink_socket(node.outputs[0], new_output)

                    node.inputs.remove(node.inputs[0])
                    node.outputs.remove(node.outputs[0])

    def relink_socket(self, old_socket, new_socket):
        '''Utility function to relink sockets'''
        if not old_socket.is_output and not new_socket.is_output and old_socket.links:
            self.links.new(old_socket.links[0].from_socket, new_socket)
            self.links.remove(old_socket.links[0])
        elif old_socket.is_output and new_socket.is_output and old_socket.links:
            links = list(old_socket.links[:])
            for link in links:
                self.links.new(new_socket, link.to_socket)
                # self.links.remove(link)

    def execute(self, context):
        task_node = self.nodes.get(bpy.context.window_manager.sp_viewer_node)
        if not task_node: return

        runtime_info['executing'] = True
        cache_socket_variables.clear()

        id = str(uuid.uuid4())
        path = []

        try:
            path.append(bpy.context.space_data.node_tree.name)
            # Execute all the parent trees first up to their active node
            for i in range(0, len(bpy.context.space_data.path) - 1):
                node = bpy.context.space_data.path[i].node_tree.nodes.active
                node.execute_dependants(bpy.context, id, path)
                path.append(node.name)

            task_node.execute(bpy.context, id, path)
        except Exception as e:
            print(e)

        finally:
            runtime_info['executing'] = False





class PearlNodeTree(NodeTreeBase):
    bl_idname = 'PearlNodeTree'
    bl_label = "Pearl Editor"
    bl_icon = "COLORSET_04_VEC"

class PearlNodeTreeGroup(NodeTreeBase):
    bl_idname = 'PearlNodeTreeGroup'
    bl_label = "Pearl Node Group"
    bl_icon = "NODETREE"

    @classmethod
    def poll(cls, context):
        return False



# 注册与卸载
classes = [
    PearlNodeTree,
    PearlNodeTreeGroup

]

def register():
    for c in classes:
        bpy.utils.register_class(c)
        
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)