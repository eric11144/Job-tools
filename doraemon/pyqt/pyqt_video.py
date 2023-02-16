# -*- coding: utf-8 -*-
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class VideoWindow(QMainWindow):
     def __init__(self):
        super(VideoWindow, self).__init__()
        self.setWindowTitle('QMediaPlayer TEST')
        self.resize(640, 480)

        self.videoItem =  QGraphicsVideoItem()
        


        # QMediaPlayer
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/home/ubuntu/videoplayback.mp4')))

        # Set widget
        self.videoWidget = QVideoWidget()
        self.videoWidget.setGeometry(10,180,220,160)
        self.setCentralWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Play
        self.mediaPlayer.play()

        self.setGeometry(500,200,1200,500)


if __name__ == '__main__':
     app = QApplication([])
     window = VideoWindow()
     window.show()
     sys.exit(app.exec_())