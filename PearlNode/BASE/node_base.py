import bpy

from .runtime import *

class NodeBase(bpy.types.Node):
    bl_label = "NodeBase"

    # 只在节点树/节点组中才能操作节点
    @classmethod
    def poll(cls,context):
        return context.bl_idname in {'NodeTree','NodeTreeGroup'}


    # input & output socket
    def create_input(self, socket_type, socket_name, socket_label, default_value=None):
        pass

    def remove_input(self, socket_name):
        pass

    def create_output(self, socket_type, socket_name, socket_label, default_value=None):
        pass

    def remove_output(self, socket_name):
        pass

    # execute
    def execute(self, context, id, path):
        pass

    # others
    def draw_buttons(self, context, layout):
        pass

    def update(self):
        if runtime_info['updating'] is True:
            return






def register():
    bpy.utils.register_class(NodeBase)


def unregister():
    bpy.utils.unregister_class(NodeBase)
