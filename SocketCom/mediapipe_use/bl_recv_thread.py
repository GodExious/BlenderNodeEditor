import socket
import threading
import time
import bpy

'''
TODO
如果要设计为operator子类该如何写？
必须要有context环境才能进行ops操作
如何解决这个问题
'''

class Recv():
    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口

    def receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口
        while True:
            data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址  
            if data.decode() == '###':  # 自定义结束字符串
                break
            self.run(data)
        self.s.close()

    def run(self,data):
        recv_str = data.decode()
        recv = recv_str.split()
        for i in range(len(recv)):
            recv[i] = float(recv[i])
        print('[Recieved]', recv)

        #bpy.context.scene.objects['Cube'].location[0] = recv[0]
        #bpy.context.scene.objects['Cube'].location[1] = recv[1]
        bpy.data.objects['bone'].pose.bones['Bone.001'].rotation_quaternion[1] = (recv[1]-10)/5
        

if __name__ == "__main__":
    recv = Recv()
    p = threading.Thread(target = recv.receive)
    p.setDaemon(True)
    p.start()
    
    #p.join()
    



