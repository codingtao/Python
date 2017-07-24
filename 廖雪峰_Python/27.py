# 客户端程序

import socket

# 创建一个IPV4 面向流的SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1',9995))

print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()