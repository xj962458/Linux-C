from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

app=QApplication([])
window=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(window)
app.exec_()
