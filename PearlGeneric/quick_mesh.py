import bpy
import bmesh
# import cv2
from mathutils import Vector, Matrix, Quaternion


class QUICK_OT_mesh_add(bpy.types.Operator):
    bl_idname = 'pearl.quick_mesh_add'
    bl_label = 'test mesh add'
    # 'UNDO'
    bl_options = {'REGISTER','UNDO'}

    mesh_height : bpy.props.FloatProperty(name="height",default=2)
    mesh_bottom_size : bpy.props.FloatProperty(name="bottom size",default=1)

    def mesh_add_Pyramid(self):
        verts = [(1*self.mesh_bottom_size,1*self.mesh_bottom_size,0),
                (-1*self.mesh_bottom_size,1*self.mesh_bottom_size,0),
                (-1*self.mesh_bottom_size,-1*self.mesh_bottom_size,0),
                (1*self.mesh_bottom_size,-1*self.mesh_bottom_size,0),
                (0,0,self.mesh_height)]
        edges = [(0,1),
                (1,2),
                (2,3),
                (3,0),
                (0,4),
                (1,4),
                (2,4),
                (3,4)]
        faces = [(0,1,4),
                (1,2,4),
                (2,3,4),
                (3,0,4),
                (0,1,2,3)]

        mesh = bpy.data.meshes.new('Pyramid_Mesh') # 新建网格
        mesh.from_pydata(verts, edges, faces)      # 载入网格数据
        mesh.update()                              # 更新网格数据

        pyramid=bpy.data.objects.new('Pyramid', mesh) # 使用mesh 新建object
        bpy.data.collections["Collection"].objects.link(pyramid)

    def execute(self, context):
        self.mesh_add_Pyramid()
        self.report({"INFO"},"test mesh add")
        return {'FINISHED'}

    # def invoke(self,context,event):
    #     return context.window_manager.invoke_props_dialog(self)

    # def draw(self,context):
    #     layout = self.layout
    #     row = layout.row()
    #     row.prop(self,"mesh_height",icon="BLENDER",text="Mesh Height")

class QUICK_OT_mesh_move(bpy.types.Operator):
    bl_idname = 'pearl.quick_mesh_move'
    bl_label = 'test mesh move by bmesh'
    bl_options = {'REGISTER','UNDO'}

    mesh_move_towards : bpy.props.IntProperty(
        name="towards",
        max=2,      # x y z
        min=0,
        default=0
        )
    mesh_move_distance : bpy.props.FloatProperty(
        name="distance",
        default=0)

    def mesh_move(self):
        obj = bpy.context.active_object
        if obj.type != 'MESH':
            return
        # 进入编辑模式
        # bpy.ops.object.editmode_toggle()
        bpy.ops.object.mode_set(mode="EDIT")

        # Get a BMesh representation
        bm = bmesh.from_edit_mesh(obj.data)

        # Modify the BMesh
        for v in bm.verts:
            v.co[self.mesh_move_towards] += self.mesh_move_distance

        # test
        '''
        vert1 = bm.verts.new(Vector((0,0,-2)))
        vert2 = bm.verts.new(Vector((2,0,-2)))
        vert3 = bm.verts.new(Vector((2,0,0)))
        vert4 = bm.verts.new(Vector((0,0,0)))
        bm.faces.new([vert1,vert2,vert3,vert4])
        '''
        # Show the updates in the viewport
        # and recalculate n-gon tessellation.
        bmesh.update_edit_mesh(obj.data, loop_triangles=True)

        bpy.ops.object.mode_set(mode='OBJECT')

    def execute(self, context):
        self.mesh_move()

        self.report({"INFO"},"test mesh move")
        return {'FINISHED'}

'''
测试独立的cv进程，与blenderpython尝试通信

class QUICK_OT_cv_test(bpy.types.Operator):
    bl_idname = 'pearl.quick_cv_test'
    bl_label = 'test mesh add'
    # 'UNDO'
    bl_options = {'REGISTER'}

    def cv_test(self):
        cv2.imshow("C:/Users/Cuimi/Desktop/picture")
    
    def execute(self, context):
        self.cv_test()
        self.report({"INFO"},"cv test")
        return {'FINISHED'}
'''