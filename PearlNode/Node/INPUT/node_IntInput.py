import bpy
from ..BASE.node_base import SimpleNodeBase

def update_node(self, context):
    self.execute_tree()


class SimpleNodeIntInput(SimpleNodeBase):
    bl_idname = 'SimpleNodeIntInput'
    bl_label = 'Int Input'

    default_value: bpy.props.IntProperty(update=update_node)

    def init(self, context):
        self.create_output('SimpleNodeSocketInt', 'output', "Output")

    def draw_buttons(self, context, layout):
        layout.prop(self, 'default_value', text='')

    def process(self, context, id, path):
        self.outputs[0].set_value(self.default_value)


def register():
    bpy.utils.register_class(SimpleNodeIntInput)


def unregister():
    bpy.utils.unregister_class(SimpleNodeIntInput)