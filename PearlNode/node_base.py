import bpy
from .node_system import PearlNode,PearlNodeTree
from .node_socket import *

class testNode(PearlNode):
    bl_idname = "TEST_Node"
    bl_label = "test"

    default_value: bpy.props.FloatProperty(name='input', default=0.0)

    def init(self,context):
        self.inputs.new(NodeSocket_Float.bl_idname,name="输出",identifier = "out_put")
        self.outputs.new(NodeSocket_Float.bl_idname,name="输出",identifier = "out_put")
        

    def draw_buttons(self,context,layout):
        layout.prop(self, "default_value",text='')

    def process(self, context, id, path):
        self.outputs[0] = self.inputs[0]
        print("Process:")



class Node_InputFloat(PearlNode):
    bl_idname = "Node_InputFloat"
    bl_label = "Node_InputFloat"

    default_value: bpy.props.FloatProperty(name='input', default=0.0)
    prepare = True

    def init(self,context):
        self.inputs.new(NodeSocket_Float.bl_idname,name="input")
        self.outputs.new(NodeSocket_Float.bl_idname,name="output")


    def draw_buttons(self,context,layout):
        layout.prop(self, 'default_value', text='')


class Node_InputInt(PearlNode):
    bl_idname = "Node_InputInt"
    bl_label = "Node_InputInt"

    default_value: bpy.props.IntProperty(name='input', default=0)

    def init(self,context):
        self.inputs.new(NodeSocket_Int.bl_idname,name="input")
        self.outputs.new(NodeSocket_Int.bl_idname,name="output")


    def draw_buttons(self,context,layout):
        layout.prop(self, 'default_value', text='')


class Node_InputVector(PearlNode):
    bl_idname = "Node_InputVector"
    bl_label = "Node_InputVector"

    default_value: bpy.props.FloatVectorProperty(name='Vector', default=(0, 0, 0))

    def init(self,context):
        self.inputs.new(NodeSocket_Vector.bl_idname,name="input")
        self.outputs.new(NodeSocket_Vector.bl_idname,name="output")


    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop(self, 'default_value', text='')








classes = [
    testNode,
    Node_InputInt,
    Node_InputFloat,
    Node_InputVector,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
