# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 520, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 520, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 200, 541, 311))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, -20, 561, 311))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 91, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 521, 61))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 120, 321, 51))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 90, 131, 18))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(250, 90, 132, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 90, 132, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.widget.raise_()
        self.pushButton.raise_()
        self.label_6.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 30))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_P = QtWidgets.QMenu(self.menubar)
        self.menu_P.setObjectName("menu_P")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.addwinaction = QtWidgets.QAction(MainWindow)
        self.addwinaction.setObjectName("addwinaction")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.action_pink = QtWidgets.QAction(MainWindow)
        self.action_pink.setObjectName("action_pink")
        self.action_blue = QtWidgets.QAction(MainWindow)
        self.action_blue.setObjectName("action_blue")
        self.action_green = QtWidgets.QAction(MainWindow)
        self.action_green.setObjectName("action_green")
        self.action_black = QtWidgets.QAction(MainWindow)
        self.action_black.setObjectName("action_black")
        self.menu_F.addAction(self.actionOpen)
        self.menu_F.addAction(self.actionClose)
        self.menu_F.addAction(self.action)
        self.menu_E.addAction(self.actionEdit)
        self.menu_P.addAction(self.action_pink)
        self.menu_P.addAction(self.action_blue)
        self.menu_P.addAction(self.action_green)
        self.menu_P.addAction(self.action_black)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_P.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人体行为识别"))
        MainWindow.setWindowIcon(QtGui.QIcon('images/tubiao.ico'))
        self.pushButton.setText(_translate("MainWindow", "开始识别"))
        self.pushButton_2.setText(_translate("MainWindow", "保存"))
        self.label_3.setText(_translate("MainWindow", "显示图片"))
        self.label.setText(_translate("MainWindow", "视   频："))
        self.label_2.setText(_translate("MainWindow", "文件名字"))
        self.label_5.setText(_translate("MainWindow", "何种动作"))
        self.label_4.setText(_translate("MainWindow", "识别结果："))
        self.label_6.setText(_translate("MainWindow", "选择识别方法："))
        self.radioButton.setText(_translate("MainWindow", "flow "))
        self.radioButton_2.setText(_translate("MainWindow", "rbg"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menu_P.setTitle(_translate("MainWindow", "皮肤(&P)"))
        self.actionOpen.setText(_translate("MainWindow", "导入视频"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionClose.setText(_translate("MainWindow", "退出系统"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.action.setText(_translate("MainWindow", "开发者信息"))
        self.addwinaction.setText(_translate("MainWindow", "添加窗体"))
        self.addwinaction.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionEdit.setText(_translate("MainWindow", "管理"))
        self.actionEdit.setToolTip(_translate("MainWindow", "视频文件管理"))
        self.actionEdit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_pink.setText(_translate("MainWindow", "樱花粉"))
        self.action_pink.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_blue.setText(_translate("MainWindow", "天空蓝"))
        self.action_blue.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_green.setText(_translate("MainWindow", "原野绿"))
        self.action_green.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.action_black.setText(_translate("MainWindow", "星夜黑"))
        self.action_black.setShortcut(_translate("MainWindow", "Ctrl+H"))

