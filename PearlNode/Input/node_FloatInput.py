import bpy
from bpy.props import *
from ..BASE.node_base import NodeBase


def update_node(self, context):
    self.execute_tree()


class NodeFloatInput(NodeBase):
    bl_idname = 'NodeFloatInput'
    bl_label = 'Float Input'

    default_value: FloatProperty(update=update_node)

    def init(self, context):
        self.create_output('NodeFloatInput', 'output', "Output")

    def draw_buttons(self, context, layout):
        layout.prop(self, 'default_value', text='')

    def process(self, context, id, path):
        self.outputs[0].set_value(self.default_value)


def register():
    bpy.utils.register_class(NodeFloatInput)


def unregister():
    bpy.utils.unregister_class(NodeFloatInput)