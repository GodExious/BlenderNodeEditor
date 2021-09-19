import bpy
from .node_system import *
from .node_socket import *

'''
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

'''
class Node_InputFloat(PearlNode):
    bl_idname = "Node_InputFloat"
    bl_label = "Node_InputFloat"

    node_value : bpy.props.FloatProperty(name='Input', default=0.0)

    # can process instantly
    def is_prepared(self):
        return True

    def init(self, context):
        self.outputs.new(NodeSocket_Float.bl_idname, name="output")
        self.prepare_num = len(self.inputs)
    
    def draw_buttons(self,context,layout):
        layout.prop(self, 'node_value', text='')    


class Node_TransFloat(PearlNode):
    bl_idname = "Node_TransFloat"
    bl_label = "Node_TransFloat"

    # need one input to process
    # prepare = False

    def process(self):
        # 遍历所有输出socket
        for output in self.outputs:
            # 遍历每个socket连接的link
            for link in output.links:
                # 每个link末端的socket值被赋予为当前socket的值：传递
                socket_values[id(link.to_socket)] = socket_values[id(self.inputs[0])]


    def init(self, context):
        self.inputs.new(NodeSocket_Float.bl_idname,name="input")
        self.outputs.new(NodeSocket_Float.bl_idname, name="output")
        

    
    def draw_buttons(self,context,layout):
        pass   


'''
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

'''






classes = [
    Node_InputFloat,

    Node_TransFloat,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
