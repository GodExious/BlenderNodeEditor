import socket
import threading
import time

class Recv():
    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.address)  # 绑定服务端地址和端口
    def run(self):
        
        while True:
            data, addr = self.s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
            data = data.decode()
            print('[Recieved]', data)
            if data == '###':  # 自定义结束字符串
                break
        self.s.close()
        
        for i in range(10):
            print('2')

if __name__ == "__main__":
    recv = Recv()
    p = threading.Thread(target = recv.run)
    p.start()
    
    for i in range(10):
        print('1')
    #p.join()
    



'''
TCP
import socket
import sys
address = ('127.0.0.1', 5005)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(address)  # 尝试连接服务端
except Exception:
    print('[!] Server not found ot not open')
    sys.exit()
while True:
    trigger = input('Input: ')
    s.sendall(trigger.encode())
    data = s.recv(1024)
    data = data.decode()
    print('[Recieved]', data)
    if trigger == '###':  # 自定义结束字符串
        break
s.close()

'''
