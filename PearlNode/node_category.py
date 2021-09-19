import bpy
import nodeitems_utils
from .node_system import *
# node add to menu -------

class PearlNodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls,context):
        return context.space_data.tree_type == PearlNodeTree.bl_idname


node_categories = [
    PearlNodeCategory("1","Input",items=[
        nodeitems_utils.NodeItem('Node_InputFloat'),
        nodeitems_utils.NodeItem('Node_InputVector'),
        nodeitems_utils.NodeItem('more'),
    ]),
    PearlNodeCategory("2","Output",items=[
        nodeitems_utils.NodeItem('Node_OutputFloat'),
        nodeitems_utils.NodeItem('Node_OutputVector'),

    ]),
    PearlNodeCategory("3","Funtions",items=[
        nodeitems_utils.NodeItem('Node_TransFloat'),
        nodeitems_utils.NodeItem('Node_FunctionFloat'),
        nodeitems_utils.NodeItem('more'),
    ]),
    PearlNodeCategory("4","Convert",items=[
        nodeitems_utils.NodeItem('Node_Float2Vector'),
        nodeitems_utils.NodeItem('Node_Vector2Float'),

    ]),
]




# register -------
def register():
    try:
        nodeitems_utils.unregister_node_categories("PearlNodeCategory")
    except Exception:
        pass
    nodeitems_utils.register_node_categories("PearlNodeCategory", node_categories)



def unregister():
    nodeitems_utils.unregister_node_categories("PearlNodeCategory")
