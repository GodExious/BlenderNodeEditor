import bpy

class quickTranslate(bpy.types.Operator):
    # 需要两段字符串以点连接，不能有大写字母
    # 可以通过idname 在f3调用
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

