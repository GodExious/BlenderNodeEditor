import bpy
from .node_system import *
from .node_socket import *


class Node_FunctionFloat(PearlNode):
    bl_idname = "Node_FunctionFloat"
    bl_label = "Float Function"

    operate_type: bpy.props.EnumProperty(
        name='Type',
        items=[
            ('+', 'Add', ''),
            ('-', 'Subtract', ''),
            ('*', 'Muitiply', ''),
            ('/', 'Divide', ''),
        ],
        default='+', update=None
    )

    def init(self, context):
        self.inputs.new(NodeSocket_Float.bl_idname,name="input")
        self.inputs.new(NodeSocket_Float.bl_idname,name="input2")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output")
    
    def draw_buttons(self,context,layout):
        layout.prop(self, 'operate_type', text='')  

    def process(self):
        v1 = self.inputs[0].socket_value
        v2 = self.inputs[1].socket_value
        self.outputs[0].socket_value = eval(f'{v1} {self.operate_type} {v2}') 

class Node_TransFloat(PearlNode):
    bl_idname = "Node_TransFloat"
    bl_label = "Float Trans"

    node_value : bpy.props.FloatProperty(name='Input', default=0.0)
    
    def process(self):
        # print("process: ",self.name, self.prepare_num)
        self.outputs[0].socket_value = self.inputs[0].socket_value
        self.node_value = self.outputs[0].socket_value
                           
    def init(self, context):
        self.inputs.new(NodeSocket_Float.bl_idname,name="input")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output")
    
    def draw_buttons(self,context,layout):
        layout.prop(self, 'node_value', text='')  



classes = [
    Node_TransFloat,
    Node_FunctionFloat,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
