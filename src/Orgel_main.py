import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("Orgel_main.ui")[0]


class VideoWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Orgel")
        self.setGeometry(50, 50, 1000, 760)

        self.search_button.clicked.connect(self.loadImageFromFile)
        self.quit_button.clicked.connect(QCoreApplication.instance().quit)

        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)


    def loadImageFromFile(self):    # upload image to be measured
        self.qPixmapFileVar = QPixmap()
        self.fileName = QFileDialog.getOpenFileName(self, 'Open File', './', "Images (*.png *.xpm *.jpg)")
        self.qPixmapFileVar.load(self.fileName[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = VideoWindow()
    myWindow.show()
    app.exec_()