import bpy

# runtime
        # NOOOOOOOOOOOOO node_groups is readonly
        # qtmd readonly 浪费老子时间
tree_nodes = []
# lisf of nodes prepared to process
process_nodes = []
# lisf of value in sockets
socket_values = {}


# node system

class PearlNodeTree(bpy.types.NodeTree):
    bl_idname = 'PearlNodeTree'
    bl_label = 'Pearl Node Editor'
    bl_icon = 'NODETREE'

    # 储存所有的节点
    tree_nodes = {}
    # 储存所有要执行的节点
    process_nodes = []

    def printNodes(self):
        for node in self.tree_nodes:
            print(self.tree_nodes[node].name, \
                self.tree_nodes[node].prepare_num)


    def printProcessNodes(self):
        for node in self.process_nodes:
            print(node.name,node.prepare_num)


    def addExecuteNodes(self):
        self.tree_nodes.clear()
        self.process_nodes.clear()

        # 遍历节点
        for node in self.nodes:
            node.check_init()
            # self.tree_nodes.append(node)
            self.tree_nodes.setdefault(node.name,node)

            # 能够立即执行的节点 加入执行队列
            if node.is_prepared():
                self.process_nodes.append(node)
    

    def executeNodes(self):
        print("\n-------------- ",self.name)
        self.addExecuteNodes()
        self.printNodes()
        # self.printProcessNodes()

        # 执行队列不空，则一直执行第一个节点
        print("\n-------------- process start")
        while self.process_nodes:
            # 执行节点
            self.process_nodes[0].process()

            # 检查可执行的节点    
            # self.process_nodes[0].check_other_prepare()
            for output in self.process_nodes[0].outputs:
                for link in output.links:
                    self.tree_nodes[link.to_node.name].prepare_num -= 1
                    if self.tree_nodes[link.to_node.name].prepare_num == 0:
                        self.process_nodes.append(self.tree_nodes[link.to_node.name])


            # 删除执行完的节点
            self.process_nodes.remove(self.process_nodes[0])


class PearlNodeSocket(bpy.types.NodeSocket):
    bl_idname = 'PearlNodeSocket'
    bl_label = 'Pearl Node Socket'

    socket_color = (0.5, 0.5, 0.5, 1)
    socket_value = None

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        return self.socket_color



class PearlNode(bpy.types.Node):
    bl_idname = "PearlNode"
    bl_label = "PearlNode"

    prepare_num = None

    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == PearlNodeTree.bl_idname)

    def process(self):
        print("process: ",id(self), self.name, self.prepare_num)


    def is_prepared(self):
        if self.prepare_num==0:
            return True
        return False
        
    def check_init(self):
        self.prepare_num = len(self.inputs)


    def copy(self,node):
        pass

    def free(self):
        pass

    

    '''
    # update(self)????每次增加删除、连线节点都执行？
    def update(self):
        pass

    def todo(self):
        for input in self.inputs:
            # print(output.links)
            if input.links:
                for link in input.links:
                    node = link.from_node
                    print("     link from:",node)
                    # output link to_node
    '''







classes = [
    PearlNodeTree,
    PearlNodeSocket,
    PearlNode,

    
]




# register -------
def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)