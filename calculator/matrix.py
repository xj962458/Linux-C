from PySide2.QtWidgets import QMainWindow,QApplication
from ui.matrix_ui import Ui_MainWindow
import numpy as np

class Matrix(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.slot()
        self.show()

    def aquire_data(self):
        text1 = self.plainTextEdit.toPlainText()
        text2 = self.plainTextEdit_2.toPlainText()
        self.matrix1 = np.array(self.convert(text1))
        self.matrix2 = np.array(self.convert(text2))

    def slot(self):
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_subtract.clicked.connect(self.subtract)
        self.pushButton_time.clicked.connect(self.time)
        self.pushButton_dottime.clicked.connect(self.dottime)

    def add(self):
        self.aquire_data()
        result = self.matrix1+self.matrix2
        self.plainTextEdit_4.setPlainText(str(result))

    def subtract(self):
        self.aquire_data()
        result = self.matrix1-self.matrix2
        self.plainTextEdit_4.setPlainText(str(result))

    def time(self):
        self.aquire_data()
        result = self.matrix1*self.matrix2
        self.plainTextEdit_4.setPlainText(str(result))

    def dottime(self):
        self.aquire_data()
        result = np.dot(self.matrix1, self.matrix2)
        self.plainTextEdit_4.setPlainText(str(result))

    def convert(self, text):
        text = text.split("\n")
        l = []
        for i in text:
            l.append(list(map(int, i.split(' '))))
        return l

if __name__ == '__main__':
    app = QApplication([])
    win = Matrix()
    app.exec_()
