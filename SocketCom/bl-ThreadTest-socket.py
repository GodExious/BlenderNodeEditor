import threading
import bpy
import socket

class Recv():
    
    def __init__(self):
        self.recvFlag = 0
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口
        while True:
            data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
            data = data.decode()
            print('[Recieved]', data)
            self.recvFlag = 1
            if data == '###':  # 自定义结束字符串
                break
        self.s.close()
        

# 必须要鼠标动着modal才会循环执行？  
class test(bpy.types.Operator):
    bl_idname = "test.recv"
    bl_label = "recv"
    
    recv = Recv()
  

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if self.recv.recvFlag == 1:
            bpy.ops.transform.resize(value=(1.3,1.3,1.3))
            self.recv.recvFlag =0

    
    def invoke(self, context, event):
        
        t = threading.Thread(target = self.recv.run)
        t.start()
        context.window_manager.modal_handler_add(self)

        return { 'RUNNING_MODAL' }

    def modal (self, context, event):
        self.execute(context)

        if event.type == "LEFTMOUSE":
            self.recv.s.close()
            return {'FINISHED'}

        return {'RUNNING_MODAL'}
    

        


def register():
    bpy.utils.register_class(test)


def unregister():
    bpy.utils.unregister_class(test)


if __name__ == '__main__':
    register()
