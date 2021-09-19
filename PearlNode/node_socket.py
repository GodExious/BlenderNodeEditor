import bpy
from .node_system import *

class NodeSocket_Int(PearlNodeSocket):
    bl_idname = 'NodeSocket_Int'
    bl_label = 'NodeSocket_Int'

    socket_color = (0.45, 0.45, 0.45, 1.0)
    socket_value : bpy.props.IntProperty(default=0)

class NodeSocket_Float(PearlNodeSocket):
    bl_idname = 'NodeSocket_Float'
    bl_label = 'NodeSocket_Float'

    socket_color = (0.3, 1.0, 0.8, 1.0)
    socket_value : bpy.props.FloatProperty(default=0.0)


class NodeSocket_Vector(PearlNodeSocket):
    bl_idname = 'NodeSocket_Vector'
    bl_label = 'NodeSocket_Vector'

    socket_color = (1.0, 0.4, 0.2, 1.0)
    socket_value : bpy.props.FloatVectorProperty(default=(0, 0, 0))


class NodeSocket_String(PearlNodeSocket):
    bl_idname = 'NodeSocket_String'
    bl_label = 'NodeSocket_String'

    socket_color = (0.2, 0.7, 1.0, 1)
    socket_value : bpy.props.StringProperty(default='')

# 弃用
# 单个顶点数据
class Vert(bpy.types.PropertyGroup):
    value : bpy.props.FloatVectorProperty(default=(0.0,0.0,0.0))

# 顶点数据集
class NodeSocket_Verts(PearlNodeSocket):
    bl_idname = 'NodeSocket_Verts'
    bl_label = 'NodeSocket_Verts'

    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.CollectionProperty(type=Vert)
    is_verts = True 



classes = [
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

    Vert,
    NodeSocket_Verts,

    
]

# register -------
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)