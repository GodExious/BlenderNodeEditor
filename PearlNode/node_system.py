import bpy
import nodeitems_utils

# class PearlTreeNode:
#     @classmethod
#     def poll(cls, ntree):
#         return ntree.bl_idname == PearlNodeTree.bl_idname

class PearlNodeTree(bpy.types.NodeTree):
    bl_idname = 'PearlNodeTree'
    bl_label = 'Pearl Node Editor'
    bl_icon = 'NODETREE'

class PearlNodeSocket(bpy.types.NodeSocket):
    bl_idname = 'PearlNodeSocket'
    bl_label = 'Pearl Node Socket'

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.2, 1.0)

class PearlNode(bpy.types.Node):
    bl_idname = "PearlNode"
    bl_label = "PearlNode"

    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == PearlNodeTree.bl_idname)







classes = [
    PearlNodeTree,
    PearlNodeSocket,
    PearlNode,

    
]



# node add to menu -------

class PearlNodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls,context):
        return context.space_data.tree_type == PearlNodeTree.bl_idname


node_categories = [
    PearlNodeCategory("1","test",items=[
        nodeitems_utils.NodeItem('TEST_Node')
    ]),
    PearlNodeCategory("2","input",items=[
        nodeitems_utils.NodeItem('TEST_Node')
    ]),
    PearlNodeCategory("3","output",items=[
        nodeitems_utils.NodeItem('TEST_Node')
    ]),
    PearlNodeCategory("4","function",items=[
        nodeitems_utils.NodeItem('TEST_Node')
    ]),
]



# register -------
def register():
    try:
        nodeitems_utils.unregister_node_categories("PearlNodeCategory")
    except Exception:
        pass
    nodeitems_utils.register_node_categories("PearlNodeCategory", node_categories)
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    nodeitems_utils.unregister_node_categories("PearlNodeCategory")
    for c in classes:
        bpy.utils.unregister_class(c)