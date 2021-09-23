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

        # 执行队列不空，则一直执行第一个节点
        print("\n-------------- process start")
        while self.process_nodes:
            # 执行节点
            # TODO 节点返回True时才执行transfer以及link_num检查
            self.process_nodes[0].process()
            
            # 传递数据
            self.process_nodes[0].transfer(self.socket_values)


            # TODO process return True/False -> transfer do/not

            # 检查可执行的节点   
            for output in self.process_nodes[0].outputs:
                for link in output.links:
                    self.tree_nodes[link.to_node.name].link_num -= 1
                    if self.tree_nodes[link.to_node.name].is_prepared() == True:
                        self.process_nodes.append(self.tree_nodes[link.to_node.name])
            ''' 
            for output in self.process_nodes[0].outputs:
                for link in output.links:
                    self.tree_nodes[link.to_node.name].prepare_num -= 1
                    if self.tree_nodes[link.to_node.name].prepare_num == 0:
                        self.process_nodes.append(self.tree_nodes[link.to_node.name])
            '''


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
    link_num = None

    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == PearlNodeTree.bl_idname)

    # 已弃用、且字典不再以id为key
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
        print("process: ",id(self), self.name)
        return True

    def transfer(self, socket_values):
        # print("transfer: ",self.name)
        # 遍历所有输出socket
        for output in self.outputs:
            # 遍历每个socket连接的link
            for link in output.links:
                # 每个link末端的socket值被赋予为当前socket的值：传递
                socket_values[link.to_socket].socket_value = socket_values[link.from_socket].socket_value

    '''
    新的入度算法
    以连接的link数来判断执行时机，每次执行前置节点，link_num都减1，当link_num为0时，该节点可以执行
    除此之外还有一个最小执行要求，即is_prepared()函数中需要定义的必须连接的socket，否则不执行

    '''
    def is_prepared(self):
        # return self.prepare_num==0
        return self.link_num == 0

        
    def check_init(self):
        self.prepare_num = len(self.inputs)
        # 目前连接的所有link，即前置需要执行的所有socket
        self.link_num = 0
        for input in self.inputs:
            self.link_num += len(input.links)


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