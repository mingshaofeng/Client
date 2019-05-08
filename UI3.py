import sys,pymysql

from functools import partial
from PyQt5.Qt import QWidget
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame,QApplication,QDialog, QDialogButtonBox,
        QMessageBox,QVBoxLayout, QLineEdit,QTableWidgetItem,QTableWidget,QHBoxLayout,QHeaderView)
import qtawesome

class Table_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("数据库列表")
        self.resize(1000,800)
        self.setObjectName('win')


        self.setWindowIcon(QtGui.QIcon('images/tubiao.ico'))




        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='MSF', password='1024161X', db='videos',
                             charset='utf8', )
        self.cur = self.db.cursor()
        self.cur.execute("select name,url,mark from video")
        self.data = self.cur.fetchall()


        self.col_lst = [tup[0] for tup in self.cur.description]
        row = len(self.data)
        vol = len(self.data[0])


        self.MyTable = QTableWidget(row,vol)
        font = QtGui.QFont('微软雅黑',10)

        self.MyTable.horizontalHeader().setFont(font)
        self.MyTable.setHorizontalHeaderLabels(self.col_lst)
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.setFrameShape(QFrame.NoFrame)
        self.MyTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MyTable.horizontalHeader().setStyleSheet('QHeaderView::section{background:skyblue}')

        for i in range(row):
            for j in range(vol):
                temp_data = self.data[i][j]
                data1 = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.MyTable.setItem(i, j, data1)

        #编辑按钮
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.qle = QLineEdit()
        self.qle.setPlaceholderText("输入视频名称、动作数字标签，QUERY键进行搜索")
        buttonBox = QDialogButtonBox()
        #增删查改四个按钮
        self.addButton = buttonBox.addButton("&ADD",QDialogButtonBox.ActionRole)
        self.okButton = buttonBox.addButton("&OK",QDialogButtonBox.ActionRole)
        self.deleteButton = buttonBox.addButton("&DELETE",QDialogButtonBox.ActionRole)
        self.inquireButton = buttonBox.addButton("&QUERY",QDialogButtonBox.ActionRole)
        #按钮的颜色优化
        self.addButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{
        background:red;}''')
        self.okButton.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{
        background:yellow;}''')
        self.deleteButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{
        background:green;}''')
        self.inquireButton.setStyleSheet('''QPushButton{background:#CC6699;border-radius:5px;}QPushButton:hover{
        background:blue;}''')
        self.qle.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }'''
        )


        #设置按钮内字体样式
        self.addButton.setFont(font)
        self.okButton.setFont(font)
        self.deleteButton.setFont(font)
        self.inquireButton.setFont(font)

        #网格布局
        self.net_widget = QtWidgets.QWidget()
        self.net_layout = QtWidgets.QGridLayout()#搜索部件的布局
        self.net_widget.setLayout(self.net_layout)
        self.net_layout.addWidget(self.search_icon,0,0,1,1)
        self.net_layout.addWidget(self.qle,0,1,1,8)


        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.net_widget)
        #layout.addWidget(self.search_icon)
        #layout.addWidget(self.qle)
        layout.addWidget(buttonBox)
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        #qss进行布局优化
        self.setStyleSheet("#win{background-color: white}")#设置背景为白色
        self.setWindowOpacity(0.9)#设置透明度
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        layout.setSpacing(0)
        self.setStyleSheet('''
        #win{
            background:white;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        ''')




if __name__=='__main__':
    app = QApplication(sys.argv)
    example = Table_UI()

    example.show()
    sys.exit(app.exec_())