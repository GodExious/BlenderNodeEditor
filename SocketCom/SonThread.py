import threading
import socket
import bpy


class test(bpy.types.Operator):
    bl_idname = "test.change"
    bl_label = "test"

    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.t = threading.Thread(target = self.receive)

    def receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口
        while True:
            data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
            self.run(data)
            if data == '###':  # 自定义结束字符串
                break
        self.s.close()
    def run(self,data):
        recv_str = data.decode()
        recv = recv_str.split()
        for i in range(len(recv)):
            recv[i] = int(recv[i])
        print('[Recieved]', recv)

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        # self.receive()
        
        self.t.setDaemon(True)
        self.t.start()
        return {'FINISHED'}
        '''
        if self.recv.recvFlag == 1:
            bpy.ops.transform.resize(value=(1.3,1.3,1.3))
            self.recv.recvFlag =0
        '''

def func():
    while True:
        print(1)



def register():
    bpy.utils.register_class(test)


def unregister():
    bpy.utils.unregister_class(test)


if __name__ == '__main__':
    register()
    
