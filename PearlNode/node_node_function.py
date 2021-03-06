import bpy
from .node_system import *
from .node_socket import *


class Node_FunctionFloat(PearlNode):
    bl_idname = "Node_FunctionFloat"
    bl_label = "Float Math"

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


class Node_FunctionVector(PearlNode):
    bl_idname = "Node_FunctionVector"
    bl_label = "Vector Math"

    operate_type: bpy.props.EnumProperty(
        name='Type',
        items=[
            ('+', 'Add', ''),
            ('-', 'Subtract', ''),
            ('dot', 'Dot Product', ''),
            ('cross', 'Cross Product', ''),
            ('project', 'Project', ''),
            ('normalized', 'Normalized', ''),
            ('length', 'Length', ''),
        ],
        default='+', update=None
    )

    def init(self, context):
        self.inputs.new(NodeSocket_Vector.bl_idname,name="input")
        self.inputs.new(NodeSocket_Vector.bl_idname,name="input2")
        self.outputs.new(NodeSocket_Vector.bl_idname, name="output")
    
    def draw_buttons(self,context,layout):
        layout.prop(self, 'operate_type', text='')  

    def process(self):
        v1 = self.inputs[0].socket_value
        v2 = self.inputs[1].socket_value
        result = None

        # can not support

        if self.operate_type == '+':
            result = v1 + v2
        elif self.operate_type == '-':
            result = v1 - v2
        elif self.operate_type == 'dot':
            result = v1.dot(v2)
        elif self.operate_type == 'cross':
            result = v1.cross(v2)
        elif self.operate_type == 'project':
            result = v1.project(v2)
        elif self.operate_type == 'normalized':
            result = v1.normalized()
        elif self.operate_type == 'length':
            result = v1.length

        self.outputs[0].socket_value = result


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
    Node_FunctionVector,


]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
