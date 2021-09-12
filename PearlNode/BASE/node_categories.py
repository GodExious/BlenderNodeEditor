import nodeitems_utils

class NodeCategory(nodeitems_utils.NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type in {'NodeTree','NodeTreeGroup'}

node_categories = [
    NodeCategory('INPUT',"Input",items=[
        nodeitems_utils.NodeItem('Test'),
    ]),
    NodeCategory('OUTPUT',"Output",items=[
        nodeitems_utils.NodeItem('Test'),
    ]),

]



def register():
    try:
        nodeitems_utils.unregister_node_categories("NodeCategory")
    except Exception:
        pass
    nodeitems_utils.register_node_categories("NodeCategory", node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories("NodeCategory")