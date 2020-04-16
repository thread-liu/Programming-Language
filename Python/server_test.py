# 导入 socket、sys 模块
import socket
import sys

def socket_server():
    # 创建 socket 对象
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print("the server ip is ",ip)
    # 监听所有IP
    # host = 0.0.0.0
    # 服务端口
    port = 9999
    # 绑定端口号
    serversocket.bind(('0.0.0.0', port))
    # 设置最大连接数，超过后排队
    serversocket.listen(5)

    while True:
        # 建立客户端连接
        
        clientsocket,addr = serversocket.accept()      

        print("连接地址: %s" % str(addr))
        
        msg='welcome to Chian！'+ "\r\n"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()
socket_server()