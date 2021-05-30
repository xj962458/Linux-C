from PySide2.QtWidgets import QApplication, QMainWindow
from ui.UI import Ui_mainWindow
from matrix import Matrix
from set import Set


class MyApp(Ui_mainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.slot()
        self.shortcut()

    def slot(self):
        self.pushButton_4.clicked.connect(self.pushbutton_i)  # i
        self.pushButton_7.clicked.connect(self.pushbutton_lbracket)  # (
        self.pushButton_8.clicked.connect(self.pushbutton_rbracket)  # )
        self.pushButton_13.clicked.connect(self.pushbutton_clear)  # AC
        self.pushButton_6.clicked.connect(self.pushbutton9)  # 9
        self.pushButton_5.clicked.connect(self.pushbutton8)  # 8
        self.pushButton_3.clicked.connect(self.pushbutton7)  # 7
        self.pushButton_2.clicked.connect(self.pushbutton6)  # 6
        self.pushButton_9.clicked.connect(self.pushbutton5)  # 5
        self.pushButton_10.clicked.connect(self.pushbutton4)  # 4
        self.pushButton_12.clicked.connect(self.pushbutton3)  # 3
        self.pushButton_11.clicked.connect(self.pushbutton2)  # 2
        self.pushButton.clicked.connect(self.pushbutton1)  # 1
        self.pushButton_17.clicked.connect(self.pushbutton0)  # 0
        self.pushButton_19.clicked.connect(self.pushbutton_equal)  # ＝
        self.pushButton_18.clicked.connect(self.pushbutton_dot)  # .
        self.pushButton_20.clicked.connect(self.pushbutton_add)  # ＋
        self.pushButton_16.clicked.connect(self.pushbutton_subtract)  # -
        self.pushButton_15.clicked.connect(self.pushbutton_time)  # ×
        self.pushButton_14.clicked.connect(self.pushbutton_divide)  # ÷
        self.pushButton_21.clicked.connect(self.matrix_ui)  # 矩阵运算
        self.pushButton_22.clicked.connect(self.set_ui)  # 集合运算
        self.pushButton_24.clicked.connect(self.del_ch)  # 删除

    def shortcut(self):
        self.pushButton_4.setShortcut('i')  # On/OFF
        self.pushButton_7.setShortcut('(')  # (
        self.pushButton_8.setShortcut(')')  # )
        self.pushButton_13.setShortcut('c')  # AC
        self.pushButton_6.setShortcut('9')  # 9
        self.pushButton_5.setShortcut('8')  # 8
        self.pushButton_3.setShortcut('7')  # 7
        self.pushButton_2.setShortcut('6')  # 6
        self.pushButton_9. setShortcut('5')  # 5
        self.pushButton_10.setShortcut('4')  # 4
        self.pushButton_12.setShortcut('3')  # 3
        self.pushButton_11.setShortcut('2')  # 2
        self.pushButton.setShortcut('1')  # 1
        self.pushButton_17.setShortcut('0')  # 0
        self.pushButton_19.setShortcut('return')  # ＝
        self.pushButton_18.setShortcut('.')  # .
        self.pushButton_20.setShortcut('+')  # ＋
        self.pushButton_16.setShortcut('-')  # -
        self.pushButton_15.setShortcut('*')  # ×
        self.pushButton_14.setShortcut('/')  # ÷
        self.pushButton_24.setShortcut('backspace')

    def matrix_ui(self):
        self.m = Matrix()

    def set_ui(self):
        self.s = Set()

    def del_ch(self):
        text = self.textBrowser.toPlainText()
        self.textBrowser.setText(text[0:len(text)-1])

    def pushbutton_i(self):
        self.textBrowser.insertPlainText('i')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_lbracket(self):
        self.textBrowser.insertPlainText('(')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_rbracket(self):
        self.textBrowser.insertPlainText(')')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_clear(self):
        self.textBrowser.clear()

    def pushbutton_c(self):
        pass

    def pushbutton1(self):
        self.textBrowser.insertPlainText('1')
        self.textBrowser.ensureCursorVisible()

    def pushbutton2(self):
        self.textBrowser.insertPlainText('2')
        self.textBrowser.ensureCursorVisible()

    def pushbutton3(self):
        self.textBrowser.insertPlainText('3')
        self.textBrowser.ensureCursorVisible()

    def pushbutton4(self):
        self.textBrowser.insertPlainText('4')
        self.textBrowser.ensureCursorVisible()

    def pushbutton5(self):
        self.textBrowser.insertPlainText('5')
        self.textBrowser.ensureCursorVisible()

    def pushbutton6(self):
        self.textBrowser.insertPlainText('6')
        self.textBrowser.ensureCursorVisible()

    def pushbutton7(self):
        self.textBrowser.insertPlainText('7')
        self.textBrowser.ensureCursorVisible()

    def pushbutton8(self):
        self.textBrowser.insertPlainText('8')
        self.textBrowser.ensureCursorVisible()

    def pushbutton9(self):
        self.textBrowser.insertPlainText('9')
        self.textBrowser.ensureCursorVisible()

    def pushbutton0(self):
        self.textBrowser.insertPlainText('0')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_dot(self):
        self.textBrowser.insertPlainText('.')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_add(self):
        self.textBrowser.insertPlainText('＋')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_subtract(self):
        self.textBrowser.insertPlainText('-')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_time(self):
        self.textBrowser.insertPlainText('×')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_divide(self):
        self.textBrowser.insertPlainText('÷')
        self.textBrowser.ensureCursorVisible()

    def pushbutton_equal(self):
        self.textBrowser.insertPlainText('=')
        self.textBrowser.ensureCursorVisible()
        text = self.textBrowser.toPlainText()
        text = text.replace("\n", '').replace("＋", '+').replace(
            '=', '').replace('÷', '/').replace('×', '*').replace('i', 'j')
        try:
            result = eval(text)
            self.textBrowser.append(str(result))
        except:
            self.textBrowser.clear()
            self.textBrowser.append("False")


if __name__ == '__main__':
    app = QApplication([])
    win = MyApp()
    win.show()
    app.exec_()
