import bpy
from .node_system import *
from .node_socket import *

'''
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

'''
class Node_Float2Vector(PearlNode):
    bl_idname = "Node_Float2Vector"
    bl_label = "Float2Vector"

    node_value : bpy.props.FloatVectorProperty(name='Vector', default=(0, 0, 0))


    def init(self, context):
        self.inputs.new(NodeSocket_Float.bl_idname, name="input1")
        self.inputs.new(NodeSocket_Float.bl_idname, name="input2")
        self.inputs.new(NodeSocket_Float.bl_idname, name="input3")
        self.outputs.new(NodeSocket_Vector.bl_idname, name="output")

    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop(self, 'node_value', text='')

    def process(self):
        self.outputs[0].socket_value[0] = self.inputs[0].socket_value
        self.outputs[0].socket_value[1] = self.inputs[1].socket_value
        self.outputs[0].socket_value[2] = self.inputs[2].socket_value
        self.node_value = self.outputs[0].socket_value


        


class Node_Vector2Float(PearlNode):
    bl_idname = "Node_Vector2Float"
    bl_label = "Vector2Float"

    node_value : bpy.props.FloatVectorProperty(name='Vector', default=(0, 0, 0))

    def init(self,context):
        self.inputs.new(NodeSocket_Vector.bl_idname, name="input")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output1")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output2")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output3")

    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop(self, 'node_value', text='')

    def process(self):
        self.outputs[0].socket_value = self.inputs[0].socket_value[0]
        self.outputs[1].socket_value = self.inputs[0].socket_value[1]
        self.outputs[2].socket_value = self.inputs[0].socket_value[2]
        self.node_value = self.inputs[0].socket_value




classes = [
    Node_Float2Vector,
    Node_Vector2Float,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
