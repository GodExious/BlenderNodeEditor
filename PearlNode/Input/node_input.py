import bpy
from ..BASE.node_base import NodeBase


def update_node(self, context):
    self.execute_tree()


class NodeFloatInput(NodeBase):
    bl_idname = 'NodeFloatInput'
    bl_label = 'Float Input'

    default_value: bpy.props.FloatProperty(update=update_node)

    def init(self, context):
        self.create_output('PearlNodeSocketFloat', 'output', "Output")

    def draw_buttons(self, context, layout):
        layout.prop(self, 'default_value', text='')

    def process(self, context, id, path):
        self.outputs[0].set_value(self.default_value)

class NodeStringInput(NodeBase):
    bl_idname = 'NodeStringInput'
    bl_label = 'String Input'

    default_value: bpy.props.FloatProperty(update=update_node)

    def init(self, context):
        self.create_output('PearlNodeSocketString', 'output', "Output")

    def draw_buttons(self, context, layout):
        layout.prop(self, 'default_value', text='')

    def process(self, context, id, path):
        self.outputs[0].set_value(self.default_value)



classes = [
    NodeFloatInput,
    NodeStringInput,

]
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
