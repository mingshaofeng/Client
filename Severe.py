#接收端
import socket
import threading
import time
import sys
import os,shutil
import struct
import hashlib
import pymysql

ip_port =("10.100.124.88", 8000)#定义监听地址和端口

def socket_service():
    try:
        #定义socket连接对象
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #解决端口重用问题
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(ip_port)#绑定地址
        s.listen(5)#等待最大客户数
    except socket.error as msg:
        print(msg)#输出错误信息
        exit(1)
    print('监听开始...')

    while 1:
        conn, addr = s.accept()#等待连接
        #多线程开启
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn,addr):
    print('接收的文件来自{0}'.format(addr))
    #conn.send('欢迎连接服务器'.encode('utf-8'))

    while True:
        fileinfo_size =struct.calcsize('128sq')
        #接收文件
        buf =conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sq',buf)
            fn = filename.strip('\00'.encode('utf-8'))
            new_filename = os.path.join('./'.encode('utf-8'),fn)
            print('文件的新名字是{0}，文件的大小为{1}'.format(new_filename,filesize))


            recvd_size = 0
            m = hashlib.md5()

            fp = open(new_filename,'wb')
            print('开始接收文件...')
            pwd = os.getcwd()
            while recvd_size < filesize:
                if filesize - recvd_size > 1024:
                     data = conn.recv(1024)
                     recvd_size += len(data)
                else:
                     data = conn.recv(filesize-recvd_size)#最后一次接收
                     recvd_size += len(data)
                print('已接收：',int(recvd_size/filesize*100),'%')
                m.update(data)
                fp.write(data)#写入文件
            fp.close()

            md5_client = conn.recv(1024).decode('utf-8')
            md5_server = m.hexdigest()
          #  print("服务器发来的md5:", md5_server)
          #  print("接收文件的md5:", md5_client)
            #md5进行校验
            Str_name =str(fn,encoding='utf-8')
            path1 = pwd+'\\'+str(fn,encoding='utf-8')
            path2 = 'C:\迅雷下载'
            path3 = ('C:\迅雷下载\\'+str(fn,encoding='utf-8'))
            shutil.move(path1,path2)
            if md5_client == md5_server:
                print('接收完毕，MD5校验成功...\n')
                print('文件已存放在：'+path2)
            else:
                print('MD5验证失败')
            save_mysql(Str_name,path3,path2)
        conn.close()
        break


def save_mysql(f_name,f_url,f_mark):
    db = pymysql.connect(host='10.100.124.88', port=3306, user='MSF', password='1024161X', db='videos',
                         charset='utf8', )
    cursor = db.cursor()
    list_d = []
    list_d.append(f_name)
    list_d.append(f_url)
    list_d.append(f_mark)
    cursor.execute('insert into video(name,url,mark) values(%s,%s,%s)', list_d)
    db.commit()
    db.close()

if __name__=='__main__':
    socket_service()