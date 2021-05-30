from PySide2.QtWidgets import QMainWindow,QApplication
from ui.set_ui import Ui_MainWindow
from itertools import combinations


class Set(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.slot()
        self.show()

    def slot(self):
        self.pushButton_inter.clicked.connect(self.inter)  # 交集
        self.pushButton_union.clicked.connect(self.union)  # 并集
        self.pushButton_sub.clicked.connect(self.sub)  # 子集
        self.pushButton_diff.clicked.connect(self.diff)  # 差集

    def inter(self):
        self.aquire_data()
        str1 = str(self.set1 & self.set2)
        if str1 == 'set()':
            self.plainTextEdit_3.setPlainText('交集:{}')
        else:
            self.plainTextEdit_3.setPlainText(str1)
        self.plainTextEdit_3.ensureCursorVisible()

    def union(self):
        self.aquire_data()
        str1 = str(self.set1 | self.set2)
        if str1 == 'set()':
            self.plainTextEdit_3.setPlainText('并集{}')
        else:
            self.plainTextEdit_3.setPlainText(str1)
        self.plainTextEdit_3.ensureCursorVisible()

    def sub(self):
        self.aquire_data()
        str1 = "集合A子集:\n"+str(self.find_sub(self.set1))
        str2 = "集合B子集:\n"+str(self.find_sub(self.set2))
        if str1 == 'set()':
            self.plainTextEdit_3.setPlainText('集合A子集:{}')
        else:
            self.plainTextEdit_3.setPlainText(str1)
        if str2 == 'set()':
            self.plainTextEdit_3.appendPlainText('集合B子集:{}')
        else:
            self.plainTextEdit_3.appendPlainText(str2)
        self.plainTextEdit_3.ensureCursorVisible()

    def diff(self):
        self.aquire_data()
        str1 = "集合A-集合B:" + str(self.set1 - self.set2)
        str2 = "集合B-集合A:"+str(self.set2-self.set1)
        if str1 == 'set()':
            self.plainTextEdit_3.setPlainText('集合A-集合B:{}')
        else:
            self.plainTextEdit_3.setPlainText(str1)
        if str2 == 'set()':
            self.plainTextEdit_3.appendPlainText('集合B-集合A:{}')
        else:
            self.plainTextEdit_3.appendPlainText(str2)
        self.plainTextEdit_3.ensureCursorVisible()

    def aquire_data(self):
        text1 = self.plainTextEdit.toPlainText()
        text2 = self.plainTextEdit_2.toPlainText()
        self.set1 = set(text1.split(' '))
        self.set2 = set(text2.split(' '))

    def find_sub(self, s):
        l = []
        for a in range(len(s)):
            for i in combinations(s, a+1):
                l.append(i)
        return l


if __name__ == '__main__':
    app = QApplication([])
    win = Set()
    win.show()
    app.exec_()
