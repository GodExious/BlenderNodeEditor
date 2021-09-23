import bpy
from .node_system import *
from .node_socket import *
'''
bpy.ops.object.modifier_add(type='')

a = bpy.data.objects['Cube'].modifiers.new(name='SKIN',type='SKIN')
bpy.data.objects['Cube'].modifiers.remove(a)

表面细分 SUBSURF
蒙皮 SKIN




'''








classes = [

]


def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


