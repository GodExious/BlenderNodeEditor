import bpy
from ._runtime import *

class BaseNode(bpy.types.Node):
    bl_label = "BaseNode"

    id : bpy.props.StringProperty()

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname in {'NodeTree','NodeTreeGroup'}


    def execute(self, context, id, path):
        pass



def register():
    bpy.utils.register_class(BaseNode)


def unregister():
    bpy.utils.unregister_class(BaseNode)