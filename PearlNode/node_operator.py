import bpy
from bpy.types import Node
from .node_system import *

class PearlExecOperator(bpy.types.Operator):
    bl_idname = "pearl.node_exec"
    bl_label = "Apply"

    @classmethod
    def poll(cls, context):
        return getattr(context.space_data, 'tree_type', 'PearlNodeTree') == 'PearlNodeTree'

    def execute(self, context):
        self.executeNodeTree(context)
        return {'FINISHED'}

    def executeNodeTree(self,context):
        # 当前树 ： context.space_data.edit_tree.name
        current_tree = context.space_data.edit_tree.name
        print("\n-------------- ",current_tree)
        # 遍历节点找出能够立即执行的
        for node in bpy.data.node_groups[current_tree].nodes:
            node.check_init()
            print(node.is_prepared(),id(node),node.prepare_num)
            # 能够立即执行的节点 加入执行队列
            if node.is_prepared():
                process_nodes.append(node)
        
        # 执行队列不空，则一直执行第一个节点
        print("\n-------------- process start")
        while process_nodes:
            # 执行节点
            process_nodes[0].process()
            
            # 检查可执行的节点
            process_nodes[0].check_other_prepare()

            # 删除执行完的节点
            process_nodes.remove(process_nodes[0])

        # print("\n--------------",current_tree)



        '''
        for node in bpy.data.node_groups[current_tree].nodes:
            # print(node.prepare)
            for socket in node.outputs:
                print(id(socket))
                for link in socket.links:
                    print(id(link.to_socket))

        
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
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    bpy.types.NODE_MT_context_menu.remove(draw_menu)
