# -*- coding UTF -8 -*-
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from SP import Ui_MainWindow
from SP1 import Ui_Form
import time,threading
from PyQt5 import QtWidgets,QtCore,QtGui
import socket
import os
import hashlib
import sys
import struct
import time,threading
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from Edit import Table

global lens,fileName1
lens = 0




class Client5(QThread):
    #ip_port =("10.100.127.253", 8000)#指定要发送的服务器地址和端口

    makeprogress = pyqtSignal(int)

    def __init__(self,filename):
        super(Client5,self).__init__()
        self.filename =filename
        self.lens =0


    def run(self):
        print("222")
        ip_port = ("127.0.0.1", 8000)  # 指定要发送的服务器地址和端口
        try:
            print("socket connect!!")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 生成socket连接对象
            s.connect(ip_port)  # 连接
            print("socket")
        except socket.error as msg:
            print(msg)  # 输出错误信息
            sys.exit(1)
        print("服务器已连接...\n")
        LEN = 0
        while 1:
            #filepath = input("please input the file path:")  # 输入要发送的文件的路径
            filepath = self.filename
            if os.path.isfile(filepath):  # 如果文件存在
                # 定义文件信息，128sq（其中sq是在不同机器上的衡量单位）表示文件命长128byte
                fileinfo_size = struct.calcsize('128sq')
                # 定义文件名和文件大小
                fhead = struct.pack('128sq', os.path.basename(filepath).encode('utf-8'),
                                    os.stat(filepath).st_size)
                s.send(fhead)  # 发送文件名、文件大小等信息
                print('即将发送的文件的路径为：{0}\n'.format(filepath))
                LENS = os.stat(filepath).st_size  # 获取文件的大小
                m = hashlib.md5()
                fp = open(filepath, 'rb')  # 读取文件
                while 1:
                    #print("qq")
                    data = fp.read(1024)
                    m.update(data)
                    data_len = len(data)
                    LEN += data_len
                    if not data:
                        print('{0} 文件发送完毕...'.format(filepath))
                        break
                    s.send(data)  # 发送文件
                    global lens
                    lens = int(LEN / LENS * 100)
                    #self.makeprogress.emit(lens)
                    #time.sleep(0.0000001)
                    print('已发送：', lens, '%')
                fp.close()  # 关闭
                md5 = m.hexdigest()  # 获取MD５
                s.send(md5.encode('utf-8'))  # 发送ｍｄ５
                print('MD5:', md5)
            s.close()
            break

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)



        #菜单的点击事件，当点击关闭菜单时连接槽函数close()
        self.actionClose.triggered.connect(self.close)
        self.actionClose.setStatusTip("退出系统")
        #菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.actionOpen.triggered.connect(self.openFile)
        self.actionOpen.setStatusTip('导入视频')
        #开发者信息
        self.action.setStatusTip("橘色的猫 清水 2019.4.8")
        #子窗口
        self.addwinaction.triggered.connect(self.childShow)
        #菜单点击事件，当点击打开管理的时候连接槽函数
        self.actionEdit.triggered.connect(self.EditShow)
        self.actionEdit.setStatusTip("视频文件后台管理")




    def openFile(self):
        global fileName1
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "/Users/MING/Desktop",
                                                          "All Files (*);;Text Files (*.txt)")
        print(fileName1, filetype)
        self.statusBar.showMessage(fileName1)
        self.work = Client5(fileName1)
        if(fileName1):
            self.childShow()
            QApplication.processEvents()
            self.work.start()
            print( "work start")


    def EditShow(self):
        #文件后台管理
        self.Edit = Table()
        self.Edit.show()


    def childShow(self):
        #添加子窗口
        self.child = ChildForm()
        self.child.show()

    def load_data(self, sp):
        for i in range(1, 11):  # 模拟主程序加载过程
            time.sleep(0.3)  # 加载数据
            sp.showMessage("加载... {0}%".format(i * 10), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件

class ChildForm(QWidget,Ui_Form):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)

        #self.pushButton.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100,self)
        self.label.setStyleSheet("font:10pt '楷体';")
        self.label.setText('发送文件：\n'+fileName1)
        self.label.setGeometry(QRect(328, 240, 329, 27*4))
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignTop)
        #self.label_2.setAlignment(Qt.AlignCenter)
        #self.label_2.setScaledContents (True)
        self.gif = QMovie('images/aa.gif')
        self.label_2.setMovie(self.gif)
        self.gif.start()

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.pushButton.setText('开始')
        else:
            self.timer.start(100, self)
            self.pushButton.setText('停止')

    def timerEvent(self, e):
        if self.timer.isActive():
            pass
        else:
            self.timer.start(100,self)
        if self.step >= 100:
            self.timer.stop()
            #self.pushButton.setText('完成')
            return
        self.step=lens
        self.progressBar.setValue(self.step)



if __name__=="__main__":
    app=QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("images/time.jpg"))
    splash.showMessage("加载... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()  # 显示启动界面
    QtWidgets.qApp.processEvents()  # 处理主进程事件
    win =MainForm()
    win.load_data(splash)  # 加载数据
    win.show()
    splash.finish(win)  # 隐藏启动界面
    sys.exit(app.exec_())