# -*- coding:utf-8 -*-

import socket
import threading
import time
import sys
import os,shutil
import struct
import hashlib

ip_port2 =("192.168.69.68", 8001)#定义监听地址和端口

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
    while 1:
        conn1, addr1 = s.accept()  # 等待连接
        #多线程开始
        t = threading.Thread(target=deal_data,args=(conn1,addr1))
        t.start()
def deal_data(conn1,addr1):
        fileinfo_size = struct.calcsize('128sq')
        data = ''
        data = conn1.recv(fileinfo_size)
        data = str(data,encoding='utf-8')

        print(data)
        if(data=='1'):
            os.system('bash xxx.sh')
            os.system('bash x3.sh')
        else:
            pass


        file_txt = open('video_label.txt',mode='r')
        content =file_txt.read(20)
        print(content)
        content = bytes(content,'utf-8')
        conn1.send(content)
        conn1.close()

if __name__=='__main__':
    # socket_service2()
    socket_service2()