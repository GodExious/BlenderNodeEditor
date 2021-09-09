
import bpy
import socket

class test(bpy.types.Operator):
    bl_idname = "test.recv"
    bl_label = "recv"

    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        '''
        data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
        data = data.decode()
        print('[Recieved]', data)
        '''
        print(1)

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)

        return { 'RUNNING_MODAL' }

    def modal (self, context, event):
        self.execute(context)

        if event.type == "LEFTMOUSE":
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

def register():
        bpy.utils.register_class(test)

def unregister():
        bpy.utils.unregister_class(test)

if __name__ == '__main__':
    register()




'''


import bpy
import socket

class test(bpy.types.Operator):
    bl_idname = "test.recv"
    bl_label = "recv"

    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
        bpy.ops.transform.resize(value=(1.5,1.5,1.5))
        data = data.decode()
        print('[Recieved]', data)
        
        if data == '###':  # 自定义结束字符串
            self.s.close()
            return {'FINISHED'}   
    
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)

        return { 'RUNNING_MODAL' }

    def modal (self, context, event):
        self.execute(context)

        if event.type == "LEFTMOUSE":
            return {'FINISHED'}

        return {'RUNNING_MODAL'}  
        


def register():
        bpy.utils.register_class(test)

def unregister():
        bpy.utils.unregister_class(test)

if __name__ == '__main__':
    register()



'''


