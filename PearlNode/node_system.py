import bpy

# runtime

# lisf of nodes prepared to process
process_nodes = []
# lisf of value in sockets
socket_values = []


# node system

class PearlNodeTree(bpy.types.NodeTree):
    bl_idname = 'PearlNodeTree'
    bl_label = 'Pearl Node Editor'
    bl_icon = 'NODETREE'


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

    prepare = False # ready to process
    prepare_num = None
    test_print = 1

    @classmethod
    def poll(cls, ntree):
        return (ntree.bl_idname == PearlNodeTree.bl_idname)

    def process(self):
        print("process: ",id(self),self.prepare_num)

    def is_prepared(self):
        if self.prepare_num==0:
            return True
        return False
        

    def check_init(self):
        if self.prepare_num==None:
            self.prepare_num = len(self.inputs)

    def check_prepare(self):
        print("???",self.prepare_num)
        if self.prepare_num != None:
            self.prepare_num -= 1
            if self.prepare_num == 0:
                process_nodes.append(self)

    def check_other_prepare(self):
        for output in self.outputs:
            for link in output.links:
                link.to_node.check_prepare()
    
    def copy(self, node):
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