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


class TEST_OT_op(bpy.types.Operator):
    bl_idname = "pearl._panel"
    bl_label = "panel test"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {'REGISTER'}

    testStr : bpy.props.StringProperty(name="1",default="111")

    def execute(self, context):
        context.scene['IDFloat'] = 1.0
        return {"FINISHED"}

    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)

# 定义面板
class uiPos:
    bl_category = "Pearl"
    bl_space_type = 'VIEW_3D'  # ui_type
    bl_region_type = "UI" 
    bl_context = "objectmode"

class TEST_PT_view3d_panel(uiPos,bpy.types.Panel):
    bl_idname = "TEST_PT_view3d_panel"
    bl_label = "test"
    # 默认关闭面板
    bl_options = {"DEFAULT_CLOSED"}

    # 面板头部布局
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Head",icon="VIEW_PAN")

    # 面板布局
    def draw(self, context):
        layout = self.layout
        layout.label(text="panel test",icon="BLENDER")
        
        # 定义button 最后还可以初始化
        layout.row().operator("pearl._panel",text="召唤测试面板",icon="CUBE").testStr="init"
        layout.row().operator("pearl.quick_translate",text="一键翻译",icon="CUBE")
        layout.row().operator("pearl.quick_use",text="批量删除材质",icon="CUBE")
class TEST_PT_view3d_panel2(uiPos,bpy.types.Panel):
    bl_label = "test2"
    # 设置父级
    bl_parent_id = "TEST_PT_view3d_panel"
    # 默认关闭面板
    bl_options = {"DEFAULT_CLOSED"}

    # 面板头部布局
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Head",icon="VIEW_PAN")

    # 面板布局
    def draw(self, context):
        layout = self.layout
        layout.label(text="panel test",icon="BLENDER")
        
        # 定义button 最后还可以初始化
        layout.row().operator("pearl._panel",text="召唤测试面板",icon="CUBE").testStr="init"
        layout.row().operator("pearl.quick_translate",text="一键翻译",icon="CUBE")
        layout.row().operator("pearl.quick_use",text="批量删除材质",icon="CUBE")
        # id属性
        layout.row().prop(context.scene,'["IDFloat"]',text="test")



# 定义嵌入属性的面板
class TEST_PT_properties_panel(bpy.types.Panel):
    bl_label = "test"
    bl_options = {"HIDE_HEADER"}

    bl_space_type = 'PROPERTIES'  # ui_type
    bl_region_type = "WINDOW" 
    # 属性面板中的TEXTURE区块
    bl_context = "texture"

    # 面板布局
    def draw(self, context):
        layout = self.layout
        layout.label(text="panel test",icon="BLENDER")

# 定义文件浏览器的面板
class TEST_PT_filebrower_panel(bpy.types.Panel):
    bl_label = "test"
    bl_space_type = 'FILE_BROWSER'  # ui_type
    bl_region_type = "TOOLS" 

    # 面板布局
    def draw(self, context):
        layout = self.layout
        layout.label(text="panel test",icon="BLENDER")
        

classes = [
    MoveOperator,
    TEST_OT_op,
    TEST_PT_view3d_panel,
    TEST_PT_view3d_panel2,
    TEST_PT_properties_panel,
    TEST_PT_filebrower_panel
]

