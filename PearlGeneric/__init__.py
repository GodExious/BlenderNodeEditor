# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Operator
# from .quick_use import *
# from .quick_translate import *
from . import quick_use
from . import quick_translate
from . import test



# class TEST_OT_(bpy.types.Operator):
#     bl_idname = 'pearl.test'
#     bl_label = 'test'
#     bl_options = {'REGISTER'}

#     # property
#     value = bpy.props.FloatProperty(name='value',default=1.0)

#     @classmethod
#     def poll(params,context):
#         return True

#     def execute(self, context):
#         return {'FINISHED'}

    

bl_info = {
    "name" : "PearlGeneric",
    "author" : "Cuimi",
    "description" : "",
    "blender" : (3, 00, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "DevelopMent",
    "category" : "Test",
    "doc_url" : "",
    "tracker_url" : "https://github.com/SoTosorrow/BlenderNodeEditor",
}

# 插件开启时调用
def register():
    print("Pearl On")
    bpy.utils.register_class(quick_use.quickUse)
    bpy.utils.register_class(quick_translate.quickTranslate)
    bpy.utils.register_class(test.MoveOperator)
    bpy.utils.register_class(test.DialogTest)

# 插件关闭时调用
def unregister():
    print("Pearl Off")
    bpy.utils.unregister_class(quick_use.quickUse)
    bpy.utils.unregister_class(quick_translate.quickTranslate)
    bpy.utils.unregister_class(test.MoveOperator)
    bpy.utils.unregister_class(test.DialogTest)

'''
import bpy
# active_object
# 一键去除材质
C.scene.objs[].select_get() true or false
for obj in bpy.context.selected_objects:
    if obj.type=="MESH":
        obj.data.materials.pop()

'''