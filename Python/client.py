# 导入 socket、sys 模块
import socket
import sys


def client_test():
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # # 获取本地主机名
    # host = socket.gethostname() 
    # 设置端口号
    port = 9999


    # 连接服务，指定主机和端口
    s.connect(('192.168.10.175', port))
    print(s)
    # 接收小于 1024 字节的数据
    while True:
        msg = s.recv(1024)
        # s.close()
        print (msg.decode('utf-8'))

client_test()

