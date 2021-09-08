import bpy

class NodeBase(bpy.types.Node):
    bl_label = "NodeBase"

    id : bpy.props.StringProperty()

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname in {'NodeBase','NodeBaseGroup'}