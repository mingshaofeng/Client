#--coding=utf-8--

import socket
import threading
import time
import sys
import os,shutil
import struct
import hashlib

ip_port2 =("127.0.0.1", 8001)#定义监听地址和端口

def socket_service2():
    try:
        #定义socket连接对象
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #解决端口重用问题
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(ip_port2)#绑定地址
        s.listen(5)#等待最大客户数
    except socket.error as msg:
        print(msg)#输出错误信息
        exit(1)
    print('按钮监听开始...')
    conn1, addr1 = s.accept()  # 等待连接
    data = conn1.recv(1024)
    data = str(data,encoding='utf-8')
    print(data)

if __name__=='__main__':
    # socket_service2()
    socket_service2()