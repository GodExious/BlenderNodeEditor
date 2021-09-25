import bpy
from .node_system import *
from .node_socket import *
'''
bpy.ops.object.modifier_add(type='')

a = bpy.data.objects['Cube'].modifiers.new(name='SKIN',type='SKIN')
bpy.data.objects['Cube'].modifiers.remove(a)

表面细分 SUBSURF
蒙皮 SKIN
     a.modifiers.get('skin').branch_smoothing
    bpy.ops.object.modifier_move_to_index(modifier="skin", index=1)





'''


class Node_ModSkin(PearlNode):
    bl_idname = "Node_ModSkin"
    bl_label = "Modifier Skin"

    def process(self):
        print("process: ",self.name)
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        a = obj.modifiers.new(name='skin',type='SKIN')
        self.outputs[0].socket_value = self.inputs[0].socket_value

        # bpy.ops.object.select_all()

     # 输入物体信息
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="object")
        self.outputs.new(NodeSocket_String.bl_idname,name="object")
    # 必须连接object
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0

class Node_ModSubsurf(PearlNode):
    bl_idname = "Node_ModSubsurf"
    bl_label = "Modifier Subsurf"

    
    def process(self):
        print("process: ",self.name)
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        a = obj.modifiers.new(name='subsurf',type='SUBSURF')

        # bpy.ops.object.select_all()
        self.outputs[0].socket_value = self.inputs[0].socket_value

     # 输入物体信息
    def init(self, context):
        self.inputs.new(NodeSocket_String.bl_idname,name="object")
        self.outputs.new(NodeSocket_String.bl_idname,name="object")
    # 必须连接object
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0





# 2021-9-25
class Node_getMesh(PearlNode):
    bl_idname = "Node_getMesh"
    bl_label = "getMesh"

    def process(self):
        print("process: ",self.name)
        mesh_name = bpy.data.objects[self.inputs[0].socket_value].data.name
        self.outputs[0].socket_value = mesh_name

    def init(self, context):
        self.inputs.new(NodeSocket_Object.bl_idname,name="object")
        self.outputs.new(NodeSocket_Mesh.bl_idname,name="mesh")
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0

class Node_buildObject(PearlNode):
    bl_idname = "Node_buildObject"
    bl_label = "buildObject"

    node_value : bpy.props.StringProperty(name='object', default='')
    def draw_buttons(self,context,layout):
        col = layout.column(align=1)
        col.prop(self, 'node_value', text='Object')


    def process(self):
        print("process: ",self.name)
        # 为节省内存，删除已有的该object
        obj = bpy.data.objects.get(self.node_value)
        if obj!=None:
            bpy.data.objects.remove(obj)
        # 根据输入的mesh新建一个object
        obj = bpy.data.objects.new(self.node_value,bpy.data.meshes[self.inputs[0].socket_value])
        self.outputs[0].socket_value = obj.name

    def init(self, context):
        self.inputs.new(NodeSocket_Mesh.bl_idname,name="mesh")
        self.outputs.new(NodeSocket_Object.bl_idname,name="object")

    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0

class Node_linkObject(PearlNode):
    bl_idname = "Node_linkObject"
    bl_label = "linkObject"

    def process(self):
        print("process: ",self.name)
        obj = bpy.data.objects[self.inputs[0].socket_value]
        bpy.data.collections['Collection'].objects.link(obj)

    def init(self, context):
        self.inputs.new(NodeSocket_Object.bl_idname,name="object")
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0

class Node_addModifier_Skin(PearlNode):
    bl_idname = "Node_addModifier_Skin"
    bl_label = "Add Modifier Skin"

    def process(self):
        print("process: ",self.name)
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        a = obj.modifiers.new(name='skin',type='SKIN')

        # bpy.ops.object.select_all()
        self.outputs[0].socket_value = self.inputs[0].socket_value

     # 输入物体信息
    def init(self, context):
        self.inputs.new(NodeSocket_Object.bl_idname,name="object")
        self.outputs.new(NodeSocket_Object.bl_idname,name="object")
    # 必须连接object
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0

class Node_addModifier_Subsurf(PearlNode):
    bl_idname = "Node_addModifier_Subsurf"
    bl_label = "Add Modifier Subsurf"

    def process(self):
        print("process: ",self.name)
        obj_name = self.inputs[0].socket_value
        obj = bpy.data.objects[obj_name]
        a = obj.modifiers.new(name='subsurf',type='SUBSURF')

        # bpy.ops.object.select_all()
        self.outputs[0].socket_value = self.inputs[0].socket_value

     # 输入物体信息
    def init(self, context):
        self.inputs.new(NodeSocket_Object.bl_idname,name="object")
        self.outputs.new(NodeSocket_Object.bl_idname,name="object")
    # 必须连接object
    def is_prepared(self):
        if not self.inputs[0].is_linked:
            return False
        return self.link_num == 0


classes = [
    Node_ModSkin,
    Node_ModSubsurf,

    # new name system Node_nN
    Node_getMesh,
    Node_buildObject,
    Node_linkObject,
    Node_addModifier_Skin,
    Node_addModifier_Subsurf,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


