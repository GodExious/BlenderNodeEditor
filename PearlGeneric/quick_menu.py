import bpy
from . import quick_use
from . import quick_mesh


# 饼菜单
class QUICK_MT_QuickPie(bpy.types.Menu):
    bl_idname = "QUICK_MT_QuickPie"
    bl_label ="Pearl-QuickUse"

    def draw(self,context):
        layout = self.layout
        pie = layout.menu_pie()
        # left
        pie.operator(quick_use.QUICK_OT_material_clear.bl_idname,text="Material Clear",icon="BLENDER")
        # right
        pie.operator(quick_use.QUICK_OT_print.bl_idname,text="Hello",icon="CUBE")
        # down
        pie.operator(quick_use.QUICK_OT_translate.bl_idname,text="Translate",icon="BLENDER")
        # up
        pie.operator(quick_use.QUICK_OT_material_appoint.bl_idname,text="Material Appoint",icon="BLENDER")
        pie.operator(quick_use.QUICK_OT_clean.bl_idname,text="UnUse Clean",icon="BLENDER")
        # test
        pie.operator(quick_mesh.QUICK_OT_mesh_add.bl_idname,text="Test Mesh",icon="CUBE")
        pie.operator(quick_mesh.QUICK_OT_mesh_move.bl_idname,text="Test BMesh",icon="CUBE")
        # pie.operator(quick_mesh.QUICK_OT_cv_test.bl_idname,text="Test BMesh",icon="CUBE")


classes = [
    quick_use.QUICK_OT_material_clear,
    quick_use.QUICK_OT_material_appoint,
    quick_use.QUICK_OT_translate,
    quick_use.QUICK_OT_print,
    quick_use.QUICK_OT_clean,

    quick_mesh.QUICK_OT_mesh_add,
    quick_mesh.QUICK_OT_mesh_move,
    # quick_mesh.QUICK_OT_cv_test,

    QUICK_MT_QuickPie,
]