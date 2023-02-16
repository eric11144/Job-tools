import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QPushButton
from PyQt5.QtGui import QPixmap, QImage,QFont
from PyQt5.QtCore import QTimer

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setGeometry(300,100,200,200)
        self.label.setFont(QFont("Roman times",100,QFont.Bold))
        self.setGeometry(500,300,700,500)
        self.setWindowTitle("PyQT Timer Demo")
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.run)
        # self.timer.start(1000)
        self.total = 0
 #add start Btn
        self.startBtn = QPushButton(self)
        self.stopBtn = QPushButton(self)
        self.startBtn.clicked.connect(self.startCount)
        self.startBtn.setGeometry(50,400,100,50)
        self.startBtn.setText("Start")

        self.stopBtn.clicked.connect(self.stopCount)
        self.stopBtn.setGeometry(500,400,100,50)
        self.stopBtn.setText("Stop")

#Start the Timer
    def startCount(self):
        self.timer.start(1000)
# Stop the Timer
    def stopCount(self):
        self.timer.stop()

    def run(self):

        self.label.setText(str(self.total))
        self.total+=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())
