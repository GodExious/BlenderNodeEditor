import bpy
import bmesh
from .node_system import *
from .node_socket import *

'''
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

'''

class Node_InputObject(PearlNode):
    bl_idname = "Node_InputObject"
    bl_label = "Object Input"    

    node_value : bpy.props.StringProperty(name='object', default='')

    def init(self,context):
        self.outputs.new(NodeSocket_String.bl_idname,name="output")

    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop_search(self, 'node_value', context.scene, "objects", text='Object', icon = "OBJECT_DATA")

    def process(self):
        self.outputs[0].socket_value = self.node_value

class Node_TransfromObject(PearlNode):
    bl_idname = "Node_TransfromObject"
    bl_label = "Object Transform"

    node_value : bpy.props.FloatVectorProperty(name='Input', default=(0.0,0.0,0.0))
    
    def process(self):
        obj_name = self.inputs[0].socket_value
        self.outputs[0].socket_value = self.inputs[0].socket_value

        obj = bpy.data.objects[obj_name]
        obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")

        bm = bmesh.from_edit_mesh(obj.data)
        for v in bm.verts:
            v.co.x += self.node_value[0] 
            v.co.y += self.node_value[1] 
            v.co.z += self.node_value[2] 
        bmesh.update_edit_mesh(obj.data, loop_triangles=True)
        
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(False)

                           
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="input")
        self.outputs.new(NodeSocket_String.bl_idname,name="output")
    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop(self, 'node_value', text='')  


class Node_GetMeshPoints():
    pass

class Node_GenerateMesh():
    pass



class Node_MeshAppoint(PearlNode):
    bl_idname = "Node_MeshAppoint"
    bl_label = "MeshAppoint"

    node_value : bpy.props.StringProperty(name='object', default='')
    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop_search(self, 'node_value', context.scene, "objects", text='Object', icon = "OBJECT_DATA")

    def process(self):
        # 清空缓冲   话说为啥会保留了数据
        from_obj_name = self.inputs[0].socket_value
        to_obj_name = self.node_value

        # 进入编辑模式
        from_obj = bpy.data.objects[from_obj_name]
        from_obj.select_set(True)
        to_obj = bpy.data.objects[to_obj_name]
        to_obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")

        # 获取物体bmesh
        from_obj_bm = bmesh.from_edit_mesh(from_obj.data)
        to_obj_bm = bmesh.from_edit_mesh(to_obj.data)
        to_obj_bm = from_obj_bm.copy()

# why update failed?
        # bmesh.update_edit_mesh(to_obj.data, loop_triangles=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        to_obj_bm.to_mesh(to_obj.data)

        # bm2 = bmesh.new()
        # bm2.from_mesh
        # 回到物体模式
        bpy.ops.object.select_all(False)
          
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="input")






classes = [
    Node_InputObject,
    Node_TransfromObject,
    # Node_Object2Mesh,
    Node_MeshAppoint,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)




'''

class Node_MeshAppoint(PearlNode):
    bl_idname = "Node_MeshAppoint"
    bl_label = "MeshAppoint"

    node_value : bpy.props.StringProperty(name='object', default='')
    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop_search(self, 'node_value', context.scene, "objects", text='Object', icon = "OBJECT_DATA")

    def process(self):
        # 清空缓冲   话说为啥会保留了数据
        #self.outputs[0].socket_value.clear()

        # 进入编辑模式
        bpy.ops.object.mode_set(mode="EDIT")
        # 获取物体名称
        obj_name = self.node_value.socket_value
        obj = bpy.data.objects[obj_name]
        # 获取物体bmesh
        bm = bmesh.from_edit_mesh(obj.data)
        bm.clear()

        # bm2 = bmesh.new()
        # bm2.from_mesh

        for v in self.inputs[0].socket_value:
            vertex = bm.verts.add()
            vertex.value = v.value

        bmesh.update_edit_mesh(obj.data, loop_triangles=True)


        # 回到物体模式
        bpy.ops.object.mode_set(mode='OBJECT')
          
    def init(self, context):
        self.inputs.new(NodeSocket_Verts.bl_idname,name="input")

class Node_Object2Mesh(PearlNode):
    bl_idname = "Node_Object2Mesh"
    bl_label = "Object2Mesh"

    vertics : bpy.props.CollectionProperty(type=Vert)
    
    def process(self):
        # 清空缓冲   话说为啥会保留了数据
        self.vertics.clear()
        self.outputs[0].socket_value.clear()

        # 进入编辑模式
        bpy.ops.object.mode_set(mode="EDIT")
        # 获取物体名称
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        # 获取物体bmesh
        bm = bmesh.from_edit_mesh(obj.data)

        for v in bm.verts:
            vertex = self.vertics.add()
            # vertex = self.outputs[0].socket_value.add()
            vertex.value[0] = v.co.x
            vertex.value[1] = v.co.y
            vertex.value[2] = v.co.z
        for v in self.vertics:
            vertex = self.outputs[0].socket_value.add()
            vertex.value[0] = v.value[0]
            vertex.value[1] = v.value[1]
            vertex.value[2] = v.value[2]

        # test
        print("2Mesh length:",len(self.outputs[0].socket_value))
        for v in self.outputs[0].socket_value:
            print(v.value[0],v.value[1],v.value[2])

        # 回到物体模式
        bpy.ops.object.mode_set(mode='OBJECT')
          
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="input")
        self.outputs.new(NodeSocket_Verts.bl_idname,name="output")
    




'''