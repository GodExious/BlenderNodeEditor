import bpy

class quickUse(bpy.types.Operator):
    # 需要两段字符串以点连接，不能有大写字母
    # 可以通过idname 在f3调用
    bl_idname = 'pearl.quick_use'
    bl_label = 'pop materials batch'

    # property
    value = bpy.props.FloatProperty(name='value',default=1.0)

    def execute(self, context):
        print("execute")
        self.report({"INFO"},"pop materials batch")

        # 批量删除材质
        for obj in context.selected_objects:
            if obj.type=="MESH":
                obj.data.materials.pop()
        
        return {'FINISHED'}

    def invoke(self, context, event):
        # if event.type == "LEFTMOUSE":
        #     self.report({"INFO"},"left mouse press")
        if self.poll(context):
            print("3d_view execute")

        # return {'FINISHED'}
        return self.execute(context)  

    @classmethod
    def poll(cls,context):
        # 检测当前视图为3d视图时才可以调用
        if context.area.ui_type == 'VIEW_3D':
            return True
        else:
            return False

class TEST_OT_print(bpy.types.Operator):
    bl_idname = "pearl.test"
    bl_label ="test"

    def execute(self,context):
        print('quick pie')
        return {'FINISHED'}
# 饼菜单
class TEST_MT_quickpie(bpy.types.Menu):
    bl_idname = "TEST_MT_quickpie"
    bl_label ="quick use"

    def draw(self,context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("pearl.test",text="hello",icon="CUBE")
        pie.operator("pearl.quick_translate",text="translate",icon="CUBE")


classes = [
    quickUse,
    TEST_OT_print,
    TEST_MT_quickpie,

]