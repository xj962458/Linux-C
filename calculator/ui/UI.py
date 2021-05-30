# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowDYVapa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1500, 1000)
        icon = QIcon()
        icon.addFile(u"./ui/test.ico",
                     QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        mainWindow.setIconSize(QSize(10, 10))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(
            u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.textBrowser)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_16.setFont(font1)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_16, 4, 3, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(
            self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(
            u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_12, 4, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(
            self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_15, 3, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(
            self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(
            u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_10, 3, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(
            self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(16)
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_21, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(
            self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_9, 3, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(
            self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(
            self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setFont(font2)
        self.pushButton_24.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_24, 0, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setFont(font1)
        self.pushButton_18.setStyleSheet(
            u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_18, 5, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(
            self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setFont(font1)
        self.pushButton_17.setStyleSheet(
            u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_17, 5, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(
            self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_22, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(
            self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_13, 1, 3, 1, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(
            self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setStyleSheet(
            u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_11, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(
            self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(
            self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(
            self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setFont(font1)
        self.pushButton_19.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_19, 5, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(
            self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(
            self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.pushButton_23, 0, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(
            self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setFont(font1)
        self.pushButton_20.setStyleSheet(u"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.pushButton_20, 5, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate(
            "mainWindow", u"\u7b80\u6613\u8ba1\u7b97\u5668", None))
        self.pushButton_16.setText(
            QCoreApplication.translate("mainWindow", u"-", None))
        self.pushButton_12.setText(
            QCoreApplication.translate("mainWindow", u"3", None))
        self.pushButton_15.setText(
            QCoreApplication.translate("mainWindow", u"\u00d7", None))
        self.pushButton_10.setText(
            QCoreApplication.translate("mainWindow", u"6", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("mainWindow", u"i", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("mainWindow", u"7", None))
        self.pushButton.setText(
            QCoreApplication.translate("mainWindow", u"1", None))
        self.pushButton_21.setText(QCoreApplication.translate(
            "mainWindow", u"\u77e9\u9635\u8fd0\u7b97", None))
        self.pushButton_9.setText(
            QCoreApplication.translate("mainWindow", u"5", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("mainWindow", u"(", None))
        self.pushButton_24.setText(QCoreApplication.translate(
            "mainWindow", u"\u5220\u9664", None))
        self.pushButton_18.setText(
            QCoreApplication.translate("mainWindow", u".", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("mainWindow", u"4", None))
        self.pushButton_17.setText(
            QCoreApplication.translate("mainWindow", u"0", None))
        self.pushButton_22.setText(QCoreApplication.translate(
            "mainWindow", u"\u96c6\u5408\u8fd0\u7b97", None))
        self.pushButton_13.setText(
            QCoreApplication.translate("mainWindow", u"AC", None))
        self.pushButton_14.setText(
            QCoreApplication.translate("mainWindow", u"\u00f7", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("mainWindow", u"2", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("mainWindow", u"8", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("mainWindow", u"9", None))
        self.pushButton_19.setText(
            QCoreApplication.translate("mainWindow", u"=", None))
        self.pushButton_8.setText(
            QCoreApplication.translate("mainWindow", u")", None))
        self.pushButton_23.setText(QCoreApplication.translate(
            "mainWindow", u"\u8fdb\u5236\u6362\u7b97", None))
        self.pushButton_20.setText(
            QCoreApplication.translate("mainWindow", u"+", None))
    # retranslateUi
