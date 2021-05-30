import sys,cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Video(QMainWindow):
    def __init__(self,cam):
        super().__init__()

        self.cam=cam
        self.w = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.h = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.vF=QLabel()
        self.setCentralWidget(self.vF)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(25)

    def play(self):
        r, f = self.cam.read()
        if r:
            self.vF.setPixmap(QPixmap.fromImage(
                QImage(cv2.cvtColor(f, cv2.COLOR_BGR2RGB),
                       self.w,
                       self.h,
                       13)))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Video(cv2.VideoCapture(0))
    win.show()
    sys.exit(app.exec_())