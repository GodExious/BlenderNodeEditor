import bpy
import nodeitems_utils
from .node_system import *
# node add to menu -------

class PearlNodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls,context):
        return context.space_data.tree_type == PearlNodeTree.bl_idname


node_categories = [
    PearlNodeCategory("1","input",items=[
        nodeitems_utils.NodeItem('Node_InputFloat'),
        nodeitems_utils.NodeItem('Node_InputInt'),
        nodeitems_utils.NodeItem('Node_InputVector'),
    ]),
    PearlNodeCategory("2","test",items=[
        nodeitems_utils.NodeItem('Node_TransFloat'),
        nodeitems_utils.NodeItem('Node_FunctionFloat'),
    ]),
    # PearlNodeCategory("3","output",items=[

    # ]),
    # PearlNodeCategory("4","function",items=[

    # ]),
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
