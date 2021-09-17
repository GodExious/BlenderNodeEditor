import bpy
import nodeitems_utils
from .node_run import execute_nodes

# class PearlTreeNode:
#     @classmethod
#     def poll(cls, ntree):
#         return ntree.bl_idname == PearlNodeTree.bl_idname

class PearlNodeTree(bpy.types.NodeTree):
    bl_idname = 'PearlNodeTree'
    bl_label = 'Pearl Node Editor'
    bl_icon = 'NODETREE'



class PearlNode(bpy.types.Node):
    bl_idname = "PearlNode"
    bl_label = "PearlNode"

    prepare = False # ready to process
    # id = 1

    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == PearlNodeTree.bl_idname)

    def copy(self, node):
        execute_nodes.append(self)

    def free(self):
        execute_nodes.remove(self)

    def process(self):
        print("process: ",self)
    
    def todo(self):
        for input in self.inputs:
            # print(output.links)
            if input.links:
                for link in input.links:
                    node = link.from_node
                    print("     link from:",node)

    '''
    # update(self)????每次增加删除、连线节点都执行？
    def update(self):
        pass
    '''


classes = [
    PearlNodeTree,
    PearlNode,

    
]




# register -------
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)