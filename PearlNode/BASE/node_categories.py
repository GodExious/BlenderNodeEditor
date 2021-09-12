import nodeitems_utils

class PearlNodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type in {'PearlNodeTree','PearlNodeTreeGroup'}

node_categories = [
    PearlNodeCategory('INPUT',"Input",items=[
        nodeitems_utils.NodeItem('NodeFloatInput'),
        nodeitems_utils.NodeItem('NodeStringInput'),
    ]),
    PearlNodeCategory('OUTPUT',"Output",items=[
        nodeitems_utils.NodeItem('NodeResult'),
    ]),

]



def register():
    try:
        nodeitems_utils.unregister_node_categories("PearlNodeCategory")
    except Exception:
        pass
    nodeitems_utils.register_node_categories("PearlNodeCategory", node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("PearlNodeCategory")