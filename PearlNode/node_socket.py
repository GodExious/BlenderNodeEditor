import bpy


class PearlNodeSocket(bpy.types.NodeSocket):
    bl_idname = 'PearlNodeSocket'
    bl_label = 'Pearl Node Socket'

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.2, 1.0)


class NodeSocket_Int(bpy.types.NodeSocket):
    bl_idname = 'NodeSocket_Int'
    bl_label = 'Node Socket Int'

    value : bpy.props.IntProperty()

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.45, 0.45, 0.45, 1.0)


class NodeSocket_Float(bpy.types.NodeSocket):
    bl_idname = 'NodeSocket_Float'
    bl_label = 'Pearl Node Socket Float'

    value : bpy.props.IntProperty()

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (0.3, 1.0, 0.8, 1.0)


class NodeSocket_Vector(bpy.types.NodeSocket):
    bl_idname = 'NodeSocket_Vector'
    bl_label = 'Pearl Node Socket Float'

    value : bpy.props.IntProperty()

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.2, 1.0)

classes = [
    PearlNodeSocket,

    NodeSocket_Int,
    NodeSocket_Float,
    NodeSocket_Vector,

    
]




# register -------
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)