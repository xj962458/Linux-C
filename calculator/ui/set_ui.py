# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setmZYMtL.ui'
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
        icon.addFile(u"./ui/test1.ico",
                     QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.splitter.addWidget(self.label)
        self.plainTextEdit = QPlainTextEdit(self.splitter)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.plainTextEdit.setFont(font1)
        self.splitter.addWidget(self.plainTextEdit)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy.setHeightForWidth(
            self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.splitter_2.addWidget(self.label_2)
        self.plainTextEdit_2 = QPlainTextEdit(self.splitter_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setFont(font1)
        self.splitter_2.addWidget(self.plainTextEdit_2)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy.setHeightForWidth(
            self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.splitter_3.addWidget(self.label_3)
        self.plainTextEdit_3 = QPlainTextEdit(self.splitter_3)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setFont(font1)
        self.splitter_3.addWidget(self.plainTextEdit_3)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy1)
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.pushButton_inter = QPushButton(self.splitter_4)
        self.pushButton_inter.setObjectName(u"pushButton_inter")
        sizePolicy1.setHeightForWidth(
            self.pushButton_inter.sizePolicy().hasHeightForWidth())
        self.pushButton_inter.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_inter.setFont(font2)
        self.pushButton_inter.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_4.addWidget(self.pushButton_inter)
        self.pushButton_union = QPushButton(self.splitter_4)
        self.pushButton_union.setObjectName(u"pushButton_union")
        sizePolicy1.setHeightForWidth(
            self.pushButton_union.sizePolicy().hasHeightForWidth())
        self.pushButton_union.setSizePolicy(sizePolicy1)
        self.pushButton_union.setFont(font2)
        self.pushButton_union.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_4.addWidget(self.pushButton_union)
        self.splitter_5.addWidget(self.splitter_4)
        self.splitter_6 = QSplitter(self.splitter_5)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.pushButton_sub = QPushButton(self.splitter_6)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        sizePolicy1.setHeightForWidth(
            self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy1)
        self.pushButton_sub.setFont(font2)
        self.pushButton_sub.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_6.addWidget(self.pushButton_sub)
        self.pushButton_diff = QPushButton(self.splitter_6)
        self.pushButton_diff.setObjectName(u"pushButton_diff")
        sizePolicy1.setHeightForWidth(
            self.pushButton_diff.sizePolicy().hasHeightForWidth())
        self.pushButton_diff.setSizePolicy(sizePolicy1)
        self.pushButton_diff.setFont(font2)
        self.pushButton_diff.setStyleSheet(
            u"background-color: rgb(170, 255, 0);")
        self.splitter_6.addWidget(self.pushButton_diff)
        self.splitter_5.addWidget(self.splitter_6)

        self.verticalLayout.addWidget(self.splitter_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"\u96c6\u5408\u8fd0\u7b97", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u96c6\u5408A\uff1a", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u96c6\u5408B\uff1a", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u7ed3\u679c:", None))
        self.pushButton_inter.setText(QCoreApplication.translate(
            "MainWindow", u"\u4ea4\u96c6", None))
        self.pushButton_union.setText(QCoreApplication.translate(
            "MainWindow", u"\u5e76\u96c6", None))
        self.pushButton_sub.setText(QCoreApplication.translate(
            "MainWindow", u"\u5b50\u96c6", None))
        self.pushButton_diff.setText(QCoreApplication.translate(
            "MainWindow", u"\u5dee\u96c6", None))
    # retranslateUi
