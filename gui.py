# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.afterimg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afterimg.sizePolicy().hasHeightForWidth())
        self.afterimg.setSizePolicy(sizePolicy)
        self.afterimg.setText("")
        self.afterimg.setObjectName("afterimg")
        self.gridLayout.addWidget(self.afterimg, 0, 4, 5, 1)
        self.controlvar = QtWidgets.QSlider(self.centralwidget)
        self.controlvar.setOrientation(QtCore.Qt.Vertical)
        self.controlvar.setObjectName("controlvar")
        self.gridLayout.addWidget(self.controlvar, 0, 1, 6, 1)
        self.rawimg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawimg.sizePolicy().hasHeightForWidth())
        self.rawimg.setSizePolicy(sizePolicy)
        self.rawimg.setText("")
        self.rawimg.setObjectName("rawimg")
        self.gridLayout.addWidget(self.rawimg, 0, 3, 5, 1)
        self.LogBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.LogBrowser.setObjectName("LogBrowser")
        self.gridLayout.addWidget(self.LogBrowser, 0, 5, 2, 2)
        self.InputBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputBtn.sizePolicy().hasHeightForWidth())
        self.InputBtn.setSizePolicy(sizePolicy)
        self.InputBtn.setObjectName("InputBtn")
        self.gridLayout.addWidget(self.InputBtn, 3, 5, 1, 2)
        self.Outbtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Outbtn.sizePolicy().hasHeightForWidth())
        self.Outbtn.setSizePolicy(sizePolicy)
        self.Outbtn.setObjectName("Outbtn")
        self.gridLayout.addWidget(self.Outbtn, 2, 5, 1, 2)
        self.RefreshBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefreshBtn.sizePolicy().hasHeightForWidth())
        self.RefreshBtn.setSizePolicy(sizePolicy)
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.gridLayout.addWidget(self.RefreshBtn, 4, 5, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.MenuAbout = QtWidgets.QAction(MainWindow)
        self.MenuAbout.setObjectName("MenuAbout")
        self.MenuInput = QtWidgets.QAction(MainWindow)
        self.MenuInput.setObjectName("MenuInput")
        self.MenuSwichDL = QtWidgets.QAction(MainWindow)
        self.MenuSwichDL.setObjectName("MenuSwichDL")
        self.MenuSwichTE = QtWidgets.QAction(MainWindow)
        self.MenuSwichTE.setObjectName("MenuSwichTE")
        self.MenuClose = QtWidgets.QAction(MainWindow)
        self.MenuClose.setObjectName("MenuClose")
        self.MenuOut = QtWidgets.QAction(MainWindow)
        self.MenuOut.setObjectName("MenuOut")
        self.MenuSeize = QtWidgets.QAction(MainWindow)
        self.MenuSeize.setObjectName("MenuSeize")
        self.MenuFullscreen = QtWidgets.QAction(MainWindow)
        self.MenuFullscreen.setObjectName("MenuFullscreen")
        self.MenudonotFull = QtWidgets.QAction(MainWindow)
        self.MenudonotFull.setObjectName("MenudonotFull")
        self.Menuwtlog = QtWidgets.QAction(MainWindow)
        self.Menuwtlog.setObjectName("Menuwtlog")
        self.menu.addAction(self.MenuAbout)
        self.menu.addSeparator()
        self.menu.addAction(self.MenuSeize)
        self.menu.addAction(self.MenuInput)
        self.menu.addAction(self.MenuOut)
        self.menu.addAction(self.Menuwtlog)
        self.menu.addSeparator()
        self.menu.addAction(self.MenuFullscreen)
        self.menu.addAction(self.MenudonotFull)
        self.menu.addAction(self.MenuClose)
        self.menu_2.addAction(self.MenuSwichDL)
        self.menu_2.addAction(self.MenuSwichTE)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InputBtn.setText(_translate("MainWindow", "导入"))
        self.Outbtn.setText(_translate("MainWindow", "导出"))
        self.RefreshBtn.setText(_translate("MainWindow", "刷新"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "主题"))
        self.MenuAbout.setText(_translate("MainWindow", "关于"))
        self.MenuInput.setText(_translate("MainWindow", "导入"))
        self.MenuSwichDL.setText(_translate("MainWindow", "切换深浅"))
        self.MenuSwichTE.setText(_translate("MainWindow", "选择主题"))
        self.MenuClose.setText(_translate("MainWindow", "关闭"))
        self.MenuOut.setText(_translate("MainWindow", "导出"))
        self.MenuSeize.setText(_translate("MainWindow", "缩放"))
        self.MenuFullscreen.setText(_translate("MainWindow", "全屏"))
        self.MenudonotFull.setText(_translate("MainWindow", "退出全屏"))
        self.Menuwtlog.setText(_translate("MainWindow", "导出日志"))
