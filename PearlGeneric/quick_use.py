import bpy

class QUICK_OT_MaterialClear(bpy.types.Operator):
    # 需要两段字符串以点连接，不能有大写字母
    # 可以通过idname 在f3调用
    bl_idname = 'pearl.quick_material_clear'
    bl_label = 'clear materials batch'

    def execute(self, context):
        self.report({"INFO"},"clear materials batch")

        # 批量删除材质
        for obj in context.selected_objects:
            if obj.type=="MESH":
                # old :materials.pop()
                obj.data.materials.clear()
        return {'FINISHED'}

    def invoke(self, context, event):
        if self.poll(context):
            print("3d_view execute")

        return self.execute(context)  

    @classmethod
    def poll(cls,context):
        # 检测当前视图为3d视图时才可以调用
        if context.area.ui_type == 'VIEW_3D':
            return True
        else:
            return False

class QUICK_OT_MaterialAppoint(bpy.types.Operator):
    bl_idname = 'pearl.quick_material_appoint'
    bl_label = 'appoint materials batch'

    def execute(self, context):
        # 创建新材质
        bpy.ops.material.new()

        # 批量赋予材质
        for obj in context.selected_objects:
            if obj.type=="MESH":
                # 物体激活的材质赋值为最新的材质，如果物体没有材质，则新增
                obj.active_material = bpy.data.materials[-1]

        self.report({"INFO"},"appoint materials batch")
        return {'FINISHED'}



class QUICK_OT_Translate(bpy.types.Operator):
    bl_idname = 'pearl.quick_translate'
    bl_label = 'translate CN/US'

    def execute(self, context):
        language = context.preferences.view.language
        if language == 'zh_CN':
            context.preferences.view.language = 'en_US'
        else:
            context.preferences.view.language = 'zh_CN'
        self.report({"INFO"},"translate")
        return {'FINISHED'}


class QUICK_OT_Clean(bpy.types.Operator):
    bl_idname = "pearl.unuse_clean"
    bl_label ="unuse clean"

    def execute(self,context):
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        return {'FINISHED'}


class QUICK_OT_print(bpy.types.Operator):
    bl_idname = "pearl.print"
    bl_label ="test"

    def execute(self,context):
        print('quick pie')
        return {'FINISHED'}


# 饼菜单
class QUICK_MT_QuickPie(bpy.types.Menu):
    bl_idname = "QUICK_MT_QuickPie"
    bl_label ="Pearl-QuickUse"

    def draw(self,context):
        layout = self.layout
        pie = layout.menu_pie()
        # left
        pie.operator("pearl.quick_material_clear",text="Material Clear",icon="CUBE")
        # right
        pie.operator("pearl.print",text="Hello",icon="CUBE")
        # down
        pie.operator("pearl.quick_translate",text="Translate",icon="CUBE")
        # up
        pie.operator("pearl.quick_material_appoint",text="Material Appoint",icon="CUBE")
        pie.operator("pearl.unuse_clean",text="UnUse Clean",icon="CUBE")


classes = [
    QUICK_OT_MaterialClear,
    QUICK_OT_MaterialAppoint,
    QUICK_OT_Translate,
    QUICK_OT_print,
    QUICK_OT_Clean,

    QUICK_MT_QuickPie,
]