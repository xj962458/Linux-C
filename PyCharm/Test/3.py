# window_video.py
import sys, cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
作者：杭州老王
参考：https://blog.csdn.net/oscar_liu/article/details/81210301
日期：2019-06-08、
说明：Python语言 利用PyQt5 播放USB摄像头的视频(如笔记本摄像头)
    进行了优化,以最大限度降低cpu利用率,节能环保稳定,适于持久运行
"""


class Video(QMainWindow):
    def __init__(self, cam):
        super().__init__()

        # 初始化传入的摄像头句柄为实例变量,并得到摄像头宽度和高度
        self.cam = cam
        self.w = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.h = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # 设置GUI窗口的位置和尺寸
        self.setGeometry(300, 200, self.w + 200, self.h + 200)
        self.setWindowTitle('浙江广播电视集团电视播出中心')
        # 打印得到的摄像头图像的宽和高
        print(self.w, self.h)
        self.vF = QLabel()

        self.setCentralWidget(self.vF)

        # 设置视频显示在窗口中间,否则可以注释掉
        self.vF.setAlignment(Qt.AlignCenter)

        # 设置定时器 每25毫秒执行实例的play函数以刷新图像
        self._timer = QTimer(self)
        self._timer.start(100)
        self._timer.timeout.connect(self.play)
    
        

    def play(self):
        """
        从摄像头得到图像 先转换为RGB格式 再生成QImage对象
        再用此QImage刷新vF实例变量 以刷新视频画面
        """
        r, f = self.cam.read()
        if r:
            self.vF.setPixmap(QPixmap.fromImage(
                QImage(cv2.cvtColor(f, cv2.COLOR_BGR2RGB),
                       self.w,
                       self.h,
                       13)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 初始化GUI窗口 并传入摄像头句柄
    win = Video(cv2.VideoCapture(0))
    win.show()
    sys.exit(app.exec_())
