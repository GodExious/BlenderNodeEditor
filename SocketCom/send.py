import socket
import time

class Send:
    def __init__(self):
        self.address = ('127.0.0.1', 5555)  # 服务端地址和端口
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        while True:
            for i in range(30):
                data = "hello"
                time.sleep(0.5)
                print(data)
                self.s.sendto(data.encode(), self.address)
            data = "###"
            self.s.sendto(data.encode(), self.address)
            break
        self.s.close()

if __name__ == "__main__":
    send = Send()
    send.run()

'''
TCP
import socket
address = ('127.0.0.1', 5005)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)  # 绑定服务端地址和端口
s.listen(5)
conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
print('[+] Connected with', addr)
while True:
    data = conn.recv(1024)  # buffersize 等于 1024
    data = data.decode()
    if not data:
        break
    print('[Received]', data)
    send = input('Input: ')
    conn.sendall(send.encode())
conn.close()
s.close()
'''
