import socket
import threading
import time

class Recv():
    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口

    def receive(self):
        while True:
            data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
            self.run(data)
            if data == '###':  # 自定义结束字符串
                break
        self.s.close()

    def run(self,data):
        data = data.decode()
        print('[Recieved]', data)
        

if __name__ == "__main__":
    recv = Recv()
    p = threading.Thread(target = recv.receive)
    p.setDaemon(True)
    p.start()
    
 
    #p.join()
    


