# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SP.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.setStyleSheet("#MainWindow{border-image:url(images/time.jpg);}")
        #MainWindow.setStyleSheet("#MainWindow{background-color: white}")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
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
        self.menu_F.addAction(self.actionOpen)
        self.menu_F.addAction(self.actionClose)
        self.menu_F.addAction(self.action)
        self.menu_F.addAction(self.addwinaction)
        self.menu_E.addAction(self.actionEdit)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频人体行为识别"))
        MainWindow.setWindowIcon(QtGui.QIcon('images/tubiao.ico'))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(&E)"))
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

