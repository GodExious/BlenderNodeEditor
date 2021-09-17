import bpy
from .node_system import PearlNode,PearlNodeTree,PearlNodeSocket

class testNode(PearlNode):
    bl_idname = "TEST_Node"
    bl_label = "test"

    spObject:bpy.props.StringProperty(name='object',description='选择一个物体',default='',maxlen=0,subtype='NONE',update=None,get=None,set=None);

    def init(self,context):
        self.inputs.new(PearlNodeSocket.bl_idname,name="输出",identifier = "out_put")
        self.outputs.new(PearlNodeSocket.bl_idname,name="输出",identifier = "out_put")


    def draw_buttons(self,context,layout):
        layout.prop_search(self, "spObject", context.scene, "objects", text="物体们", icon = "OBJECT_DATA");










classes = [
    testNode,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
