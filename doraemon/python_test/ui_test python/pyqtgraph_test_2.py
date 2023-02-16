import sys
import pyqtgraph as pg 

from pyModbusTCP.client import ModbusClient
from PyQt5.QtCore import Qt, QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QGridLayout, QLabel


HOST1 = "127.0.0.1"
PORT1 = 502
c1 = ModbusClient()
c1.host(HOST1)
c1.port(PORT1)
c1.unit_id(1)
data_list = []
data_list_1 = []

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.setMouseTracking(True)

        #Time init
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        
        self.lab2 = QLabel("顯示滑鼠座標", self)

        #設定界面背景顏色
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.plt = pg.plot()
        self.plt.addLegend() 

        #start bottom
        self.btn_start = QPushButton('Start', self)
        self.btn_start.clicked.connect(self.start_timer)

        #stop bottom
        self.btn_stop = QPushButton('Stop', self)
        self.btn_stop.clicked.connect(self.stop_timer)

        #quit bottom
        self.btn_quit = QPushButton('Quit', self)
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit) 

        #sample_count bottom
        self.btn_sample_count = QPushButton("樣本數")
        self.count_edit = QLineEdit("1")
        self.btn_sample_count.clicked.connect(self.getInt)

        #time bottom
        self.btn_time = QPushButton("取樣時間")
        self.time_edit = QLineEdit("")
        self.btn_time.clicked.connect(self.getTime)

        #grid_layout
        self.gridLayout = QGridLayout(self)

        #grid address
        #addWidget(*row, *column, *use_row, *use_column)
        self.gridLayout.addWidget(self.plt, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.btn_sample_count,1, 0)
        self.gridLayout.addWidget(self.count_edit,1, 1)
        self.gridLayout.addWidget(self.btn_time,2, 0)
        self.gridLayout.addWidget(self.time_edit,2, 1)
        self.gridLayout.addWidget(self.btn_start,3, 0)
        self.gridLayout.addWidget(self.btn_stop,3, 1)
        self.gridLayout.addWidget(self.btn_quit,4, 0, 1, 2) 
        self.gridLayout.addWidget(self.lab2,5,0)
        self.setLayout(self.gridLayout)

    def mouseMoveEvent(self, event):
        # if event.buttons() == Qt.LeftButton:
        #     # print(type(event.pos().x()))    #<class 'int'>
        #     self.lab2.setText(str(event.pos().x())+","+str(event.pos().y()))
        self.pos = event.pos()
        print(self.pos)
        self.lab2.setText(str(event.pos().x()) + "," + str(event.pos().y()))
        self.update()

    def drawLine(self):
        #接收 modbus server 資料
        if not c1.is_open():
            if not c1.open():
                print("unable to connect to "+HOST1+":"+str(PORT1))

        if c1.is_open():
            # read 2 registers at address 0, store result in regs list
            regs = c1.read_holding_registers(0, 50)
            data = regs[30]
            data_1 = regs[31]

            data_list.append(data)
            data_list_1.append(data_1)

            self.line_1 = self.plt.plot(
                data_list, 
                pen='r', 
                symbol='o', 
                symbolPen='b', 
                symbolBrush='w', 
                name= str(len(data_list)) + " : " + str(data)
            ) 
            self.line_2 = self.plt.plot(
                data_list_1, 
                pen='g', 
                symbol='o', 
                symbolPen='b', 
                symbolBrush='w', 
                name= str(len(data_list)) + " : " + str(data_1)
            )

        if len(data_list) == int(self.count_edit.text()):
            self.timer.stop()

    def start_timer(self):
        #更新數據取樣頻率
        if self.time_edit:
            self.timer.start(int(self.time_edit.text()))
        else:
            self.timer.start(1000)

    def stop_timer(self):
        #停止更新數據
        self.timer.stop()

    def getInt(self):
        #資料取樣數
        num,ok = QInputDialog.getInt(self, "Text Input Dialog", "輸入取樣數")
        if ok:
            self.count_edit.setText(str(num))

    def getTime(self):
        #資料取樣時間
        time,ok = QInputDialog.getInt(self, "Text Input Time", "輸入取樣時間")
        if ok:
            self.time_edit.setText(str(time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())