import bpy
from .node_run import *

class PearlExecOperator(bpy.types.Operator):
    bl_idname = "pearl.node_exec"
    bl_label = "Apply"

    @classmethod
    def poll(cls, context):
        return getattr(context.space_data, 'tree_type', 'PearlNodeTree') == 'PearlNodeTree'

    def execute(self, context):
        self.ergodicNode()
        return {'FINISHED'}

    def ergodicNode(self):
        print("--------------")
        # 遍历所有节点，找出能够执行的节点
        for node in bpy.data.node_groups['NodeTree'].nodes:
            if node.prepare == True:
                prepared_nodes.append(node)

        # 执行能够执行的节点，如果产生了新的可执行节点，则加入队列
        while(prepared_nodes):
            # 执行节点
            prepared_nodes[0].process()
            # 加入新的可执行节点
            prepared_nodes[0].todo()
            # 删除已执行的节点
            prepared_nodes.remove(prepared_nodes[0])



        '''
        for node in execute_nodes:
            print(node)
            if node.prepare == True and node not in execute_nodes:
                prepared_nodes.append(node)
        for node in prepared_nodes:
            print(node)
            node.update()
        prepared_nodes.clear()
        '''
            
        # print("node execute start")

def draw_menu(self, context):
    if context.area.ui_type == 'PearlNodeTree':
        self.layout.separator()
        self.layout.operator(PearlExecOperator.bl_idname, text="Pearl Node Exec")



classes = [
    PearlExecOperator,

]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.NODE_MT_context_menu.append(draw_menu)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    bpy.types.NODE_MT_context_menu.remove(draw_menu)
