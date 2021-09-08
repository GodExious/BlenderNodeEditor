import bpy



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


