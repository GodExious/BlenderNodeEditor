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
    # 储存所有socket
    socket_values = {}

    def printNodes(self):
        print("-------------- nodes")
        for node in self.tree_nodes:
            print(self.tree_nodes[node].name, \
                self.tree_nodes[node].prepare_num)

    def printSockets(self):
        print("-------------- sockets")
        for socket in self.socket_values:
            print(socket, \
            self.socket_values[socket].name)

    def printProcessNodes(self):
        for node in self.process_nodes:
            print(node.name,node.prepare_num)


    def addExecuteNodes(self):
        self.socket_values.clear()
        self.tree_nodes.clear()
        self.process_nodes.clear()

        # 遍历节点
        for node in self.nodes:
            node.check_init()
            # self.tree_nodes.append(node)
            self.tree_nodes.setdefault(node.name, node)

            # 能够立即执行的节点 加入执行队列
            if node.is_prepared():
                self.process_nodes.append(node)

        # 遍历socket
        for node in self.tree_nodes:
            for input in self.tree_nodes[node].inputs:
                self.socket_values.setdefault(input, input)
            for output in self.tree_nodes[node].outputs:
                self.socket_values.setdefault(output, output)
    

    def executeNodes(self):
        print("\n-------------- ",self.name)
        self.addExecuteNodes()
        self.printNodes()
        self.printSockets()
        # self.printProcessNodes()

        # 执行队列不空，则一直执行第一个节点
        print("\n-------------- process start")
        while self.process_nodes:
            # 执行节点
            self.process_nodes[0].process()
            
            # 传递数据
            self.process_nodes[0].transfer(self.socket_values)

            # 检查可执行的节点    
            # self.process_nodes[0].check_other_prepare()
            for output in self.process_nodes[0].outputs:
                for link in output.links:
                    self.tree_nodes[link.to_node.name].prepare_num -= 1
                    if self.tree_nodes[link.to_node.name].prepare_num == 0:
                        self.process_nodes.append(self.tree_nodes[link.to_node.name])

            # 删除执行完的节点
            self.process_nodes.remove(self.process_nodes[0])

        # finished
        

class PearlNodeSocket(bpy.types.NodeSocket):
    bl_idname = 'PearlNodeSocket'
    bl_label = 'Pearl Node Socket'

    socket_color = (0.5, 0.5, 0.5, 1)
    socket_value : bpy.props.IntProperty()

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


    def add_input(self, type, socket_name, value=None):
        input = self.inputs.new(type, name=socket_name)
        # if value:
        #     input.socket_value = value
        socket_values.setdefault(id(input), input)

    def add_output(self, type, socket_name, value=None):
        output = self.outputs.new(type, name=socket_name)
        socket_values.setdefault(id(output), output)

    def remove_input(self, type, socket_name, value=None):
        input = self.inputs.get(socket_name)
        if input:
            self.inputs.remove(input)
            del socket_values[id(input)]
        

    def remove_output(self, type, socket_name, value=None):
        output = self.outputs.get(socket_name)
        if output:
            self.outputs.remove(output)
            del socket_values[id(output)]

    def process(self, socket_values):
        print("process: ",id(self), self.name, self.prepare_num)

    def transfer(self, socket_values):
        print("transfer: ",self.name, self.prepare_num)
        # 遍历所有输出socket
        for output in self.outputs:
            # 遍历每个socket连接的link
            for link in output.links:
                # 每个link末端的socket值被赋予为当前socket的值：传递

                socket_values[link.to_socket].socket_value = socket_values[link.from_socket].socket_value
                # print(socket_values[link.to_socket],socket_values[link.from_socket])


    def is_prepared(self):
        return self.prepare_num==0

        
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