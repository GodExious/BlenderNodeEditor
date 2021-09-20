import bpy
import bmesh
from .node_system import *
from .node_socket import *

'''
    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,
    NodeSocket_String,

    NodeSocket_Verts,
    NodeSocket_Edges,
    NodeSocket_Faces,
    NodeSocket_Object,

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
        print("test: ",len(self.inputs[0].socket_value),len(self.inputs[1].socket_value),len(self.inputs[2].socket_value))


        # 进入编辑模式
        obj = bpy.data.objects[self.node_value]
        obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")

        # 获取物体bmesh
        # bm = bmesh.from_edit_mesh(obj.data)
        # bm.clear()
        bm = bmesh.new()


        # for v in range(len(self.inputs[0].socket_value)):
        #     vertex = bm.verts.new()
        #     vertex.co = [i for i in self.inputs[0].socket_value[v]]
        #     vertex.index = v

        # for e in range(len(self.inputs[1].socket_value)):
        #     l = [i for i in self.inputs[1].socket_value[e]]
        #     bm.verts.ensure_lookup_table()
        #     bm.edges.new([bm.verts[l[0]],bm.verts[l[1]]])
 
        # for f in range(len(self.inputs[2].socket_value)):
        #     l = [i for i in self.inputs[2].socket_value[f]]
        #     f_list = []
        #     for i in l:
        #         f_list.append(bm.verts[i])
        #     bm.faces.new(f_list)

        # 回到物体模式
        # bmesh.update_edit_mesh(obj.data, loop_triangles=True)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(False)
        bm.to_mesh(obj.data)
        bm.free()

        # self.inputs[0].socket_value.clear()
        # self.inputs[1].socket_value.clear()
        # self.inputs[2].socket_value.clear()

     
    def init(self, context):
        self.inputs.new(NodeSocket_Verts.bl_idname,name="verts")
        self.inputs.new(NodeSocket_Edges.bl_idname,name="edges")
        self.inputs.new(NodeSocket_Faces.bl_idname,name="faces")


class Node_ObjectAppoint(PearlNode):
    bl_idname = "Node_ObjectAppoint"
    bl_label = "ObjectAppoint"

    node_value : bpy.props.StringProperty(name='object', default='')
    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop_search(self, 'node_value', context.scene, "objects", text='Object', icon = "OBJECT_DATA")

    def process(self):
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        mesh = bpy.data.meshes[obj_name]
        to_obj = bpy.data.objects[self.node_value]
        # to_obj.to_mesh
        to_obj.data = mesh
        

     
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="obj")

class Node_GetObjectMesh(PearlNode):
    bl_idname = "Node_GetObjectMesh"
    bl_label = "GetObjectMesh"

    node_value : bpy.props.StringProperty(name='object', default='')
    
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop_search(self, 'node_value', context.scene, "objects", text='Object', icon = "OBJECT_DATA")

    def process(self):
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        mesh = bpy.data.meshes[obj_name]

     
    def init(self, context):
        self.inputs.new(NodeSocket_Verts.bl_idname,name="obj")


class Node_Object2BMesh(PearlNode):
    bl_idname = "Node_Object2BMesh"
    bl_label = "Object2BMesh"

    
    def process(self):
        # 清空缓冲
        self.outputs[0].socket_value.clear()
        self.outputs[1].socket_value.clear()
        self.outputs[2].socket_value.clear()

        # 进入编辑模式
        obj = bpy.data.objects[self.inputs[0].socket_value]
        obj.select_set(True)
        bpy.ops.object.mode_set(mode="EDIT")

        # 获取物体bmesh
        bm = bmesh.from_edit_mesh(obj.data)

        for v in bm.verts:
            self.outputs[0].socket_value.append([i for i in v.co])
        for e in bm.edges:
            self.outputs[1].socket_value.append([i.index for i in e.verts])
        for f in bm.faces:
            self.outputs[2].socket_value.append([i.index for i in f.verts])

# TODO 需要吗？
        # bm.free()
        
        # 回到物体模式
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(False)

        print("test output: ",len(self.outputs[0].socket_value),len(self.outputs[1].socket_value),len(self.outputs[2].socket_value))

          
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="input")
        self.outputs.new(NodeSocket_Verts.bl_idname,name="verts")
        self.outputs.new(NodeSocket_Edges.bl_idname,name="edges")
        self.outputs.new(NodeSocket_Faces.bl_idname,name="faces")
    







classes = [
    Node_InputObject,
    Node_TransfromObject,
    Node_Object2BMesh,
    Node_MeshAppoint,
    Node_ObjectAppoint,
    Node_GetObjectMesh,

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


'''