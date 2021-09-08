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
from . import quick_menu

'''
TODO 右键菜单

'''

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

# 快捷键
addon_keymaps = []


# 插件开启时调用
def register():
    print("Pearl Generic On")
    for c in quick_menu.classes:
        bpy.utils.register_class(c)

    # 注册快捷键
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # name 快捷键分区
        km = wm.keyconfigs.addon.keymaps.new(name="3D View",space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie',
            'E','PRESS',shift=False,alt=False,ctrl=False)
        kmi.properties.name = quick_menu.QUICK_MT_QuickPie.bl_idname
        addon_keymaps.append((km,kmi))

# 插件关闭时调用
def unregister():
    print("Pearl Generic Off")
    for c in quick_menu.classes:
        bpy.utils.unregister_class(c)

    # 卸载快捷键
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        for km,kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

