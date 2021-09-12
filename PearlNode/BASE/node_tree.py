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
    def get_connected_socket(self, socket):
        pass




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