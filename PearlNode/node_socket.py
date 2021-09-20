import bmesh
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






class NodeSocket_Verts(PearlNodeSocket):
    bl_idname = 'NodeSocket_Verts'
    bl_label = 'NodeSocket_Verts'

    is_part_of_bmesh = True
    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.StringProperty(default='')

        # 字符串转二维数组
    def string2list(self,st):
        list1 = st.split('%')
        result = []
        for l in list1:
            temp = l.split('@')
            temp = [float(i) for i in temp]
            result.append(temp)
        return result
    # 二维数组转字符串
    def list2string(self,l):
        result = ''
        for i in l:
            for j in i:
                result += str(j)+'@'
            result = result[:-1]
            result += '%'
        result = result[:-1]
        return result

class NodeSocket_Edges(PearlNodeSocket):
    bl_idname = 'NodeSocket_Edges'
    bl_label = 'NodeSocket_Edges'

    is_part_of_bmesh = True
    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.StringProperty(default='')

        # 字符串转二维数组
    def string2list(self,st):
        list1 = st.split('%')
        result = []
        for l in list1:
            temp = l.split('@')
            temp = [int(i) for i in temp]
            result.append(temp)
        return result
    # 二维数组转字符串
    def list2string(self,l):
        result = ''
        for i in l:
            for j in i:
                result += str(j)+'@'
            result = result[:-1]
            result += '%'
        result = result[:-1]
        return result

class NodeSocket_Faces(PearlNodeSocket):
    bl_idname = 'NodeSocket_Faces'
    bl_label = 'NodeSocket_Faces'

    is_part_of_bmesh = True
    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.StringProperty(default='')

        # 字符串转二维数组
    def string2list(self,st):
        list1 = st.split('%')
        result = []
        for l in list1:
            temp = l.split('@')
            temp = [int(i) for i in temp]
            result.append(temp)
        return result
    # 二维数组转字符串
    def list2string(self,l):
        result = ''
        for i in l:
            for j in i:
                result += str(j)+'@'
            result = result[:-1]
            result += '%'
        result = result[:-1]
        return result

class NodeSocket_Object(PearlNodeSocket):
    bl_idname = 'NodeSocket_Object'
    bl_label = 'NodeSocket_Object'

    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.StringProperty(default='')



# 即将弃用
'''
# 单个顶点数据
class Vert(bpy.types.PropertyGroup):
    value : bpy.props.FloatVectorProperty(default=(0.0,0.0,0.0))

# 顶点数据集
class NodeSocket_Verts(PearlNodeSocket):
    bl_idname = 'NodeSocket_Verts'
    bl_label = 'NodeSocket_Verts'

    socket_color = (0.8, 0.1, 0.5, 1)
    socket_value : bpy.props.CollectionProperty(type=Vert)
    socket_verts = []
    socket_edges = []
    socket_faces = []
    socket_bmesh = []
'''


classes = [
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

    NodeSocket_Verts,
    NodeSocket_Edges,
    NodeSocket_Faces,
    NodeSocket_Object,
    
]

# register -------
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)