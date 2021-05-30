# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matrixltqpEf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 1000)
        icon = QIcon()
        icon.addFile(u"./ui/test2.ico",
                     QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(10, 10))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Sunken)
        self.splitter_2.addWidget(self.label)
        self.plainTextEdit = QPlainTextEdit(self.splitter_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.plainTextEdit.setFont(font1)
        self.splitter_2.addWidget(self.plainTextEdit)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(
            self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Sunken)
        self.splitter.addWidget(self.label_2)
        self.plainTextEdit_2 = QPlainTextEdit(self.splitter)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setFont(font1)
        self.splitter.addWidget(self.plainTextEdit_2)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_6 = QSplitter(self.centralwidget)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.splitter_6.addWidget(self.label_4)
        self.plainTextEdit_4 = QPlainTextEdit(self.splitter_6)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setFont(font1)
        self.splitter_6.addWidget(self.plainTextEdit_4)

        self.verticalLayout.addWidget(self.splitter_6)

        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        sizePolicy.setHeightForWidth(
            self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy)
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.pushButton_add = QPushButton(self.splitter_3)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy.setHeightForWidth(
            self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_add.setFont(font2)
        self.pushButton_add.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_3.addWidget(self.pushButton_add)
        self.pushButton_subtract = QPushButton(self.splitter_3)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")
        sizePolicy.setHeightForWidth(
            self.pushButton_subtract.sizePolicy().hasHeightForWidth())
        self.pushButton_subtract.setSizePolicy(sizePolicy)
        self.pushButton_subtract.setFont(font2)
        self.pushButton_subtract.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_3.addWidget(self.pushButton_subtract)
        self.splitter_5.addWidget(self.splitter_3)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.pushButton_time = QPushButton(self.splitter_4)
        self.pushButton_time.setObjectName(u"pushButton_time")
        sizePolicy.setHeightForWidth(
            self.pushButton_time.sizePolicy().hasHeightForWidth())
        self.pushButton_time.setSizePolicy(sizePolicy)
        self.pushButton_time.setFont(font2)
        self.pushButton_time.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_4.addWidget(self.pushButton_time)
        self.pushButton_dottime = QPushButton(self.splitter_4)
        self.pushButton_dottime.setObjectName(u"pushButton_dottime")
        sizePolicy.setHeightForWidth(
            self.pushButton_dottime.sizePolicy().hasHeightForWidth())
        self.pushButton_dottime.setSizePolicy(sizePolicy)
        self.pushButton_dottime.setFont(font2)
        self.pushButton_dottime.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_4.addWidget(self.pushButton_dottime)
        self.splitter_5.addWidget(self.splitter_4)

        self.verticalLayout.addWidget(self.splitter_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"\u77e9\u9635\u8fd0\u7b97", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u77e9\u9635\u4e00\uff1a", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u77e9\u9635\u4e8c\uff1a", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u7ed3\u679c\uff1a", None))
        self.pushButton_add.setText(QCoreApplication.translate(
            "MainWindow", u"\u52a0\u6cd5", None))
        self.pushButton_subtract.setText(
            QCoreApplication.translate("MainWindow", u"\u51cf\u6cd5", None))
        self.pushButton_time.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e58\u6cd5", None))
        self.pushButton_dottime.setText(
            QCoreApplication.translate("MainWindow", u"\u70b9\u4e58", None))
    # retranslateUi
