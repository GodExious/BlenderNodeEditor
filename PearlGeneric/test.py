import bpy

class MoveOperator(bpy.types.Operator):
    bl_idname = "pearl.modaltest"
    bl_label = "modaltest"
    # UNDO 打开UNDO面板 ,该面板调用execute方法，要求有返回值
    bl_options = {"REGISTER","UNDO"}

    # 鼠标位置
    # 使用普通python类型是不会弹出 popu
    mouseX : bpy.props.FloatProperty(name="float",default=0)
    # mouseY : bpy.props.FloatProperty(name="float",default=0)
    # mouseX = 0.0
    mouseY = 0.0
    oldMouseX = 0.0
    oldMouseY = 0.0
    isPopu = False

    @classmethod
    def poll(cls, context):
        if context.area.ui_type == 'VIEW_3D':
            if context.object.mode == "OBJECT":
                return True
            else:
                return False
        else:
            return False

    def execute(self, context):
        # execute operator
        active_obj = context.active_object
        active_obj.location[0] = self.mouseX
        active_obj.location[1] = self.mouseY

        # execute after invoking fileselect
        if self.isPopu:
            return {"FINISHED"}

    def invoke(self, context, event):
        # init
        self.oldMouseX = context.active_object.location[0]
        self.oldMouseY = context.active_object.location[1]

        # 启动 modal : RUNNING_MODAL 调用modal
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self,context,event):
        # modal operator
        self.mouseX = event.mouse_x / 50
        self.mouseY = event.mouse_y / 50
        print(self.mouseX,self.mouseY)

        # execute operator
        self.execute(context)

        # stop modal
        if event.type == "LEFTMOUSE":
            self.isPopu = True
            return {"FINISHED"}
        if event.type in {"RIGHTMOUSE","ESC"}:
            self.mouseX = self.oldMouseX
            self.mouseY = self.oldMouseY
            self.execute(context)
            return {"CANCELLED"}
        return {'RUNNING_MODAL'}

# 弹窗 相当于popu菜单，点击ok后都是对props属性修改，执行execute
class DialogTest(bpy.types.Operator):
    bl_idname = "pearl.dialog"
    bl_label = "dialog"
    bl_options = {"REGISTER"}

    testStr : bpy.props.StringProperty(name="str",default="dialog test")

    @classmethod
    def poll(cls, context):
        return True


    def execute(self, context):
        self.report({"INFO"},"dialog Done")
        return {"FINISHED"}

    def invoke(self, context, event):
        # 弹窗
        return context.window_manager.invoke_props_dialog(self)
        # invoke_props_dialog
        # invoke_props_popup
        # invoke_popup

    # 修改布局
    def draw(self,context):
        layout = self.layout
        row = layout.row()
        row.prop(self,"testStr",icon="BLENDER",text="First Value")
