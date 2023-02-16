import sys
import pyqtgraph as pg 

from pyModbusTCP.client import ModbusClient
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtCore import Qt, QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog, QLabel, QFormLayout, QHBoxLayout, QGridLayout


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

        #Time init
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        
        # 設定界面背景顏色
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.plt = pg.plot()
        self.plt.addLegend() 

        #bottom
        self.btn_start = QPushButton('Start', self)
        # self.btn_start.move(10, 10)
        self.btn_start.clicked.connect(self.start_timer)

        self.btn_stop = QPushButton('Stop', self)
        # self.btn_stop.move(100, 10)
        self.btn_stop.clicked.connect(self.stop_timer)

        self.btn_quit = QPushButton('Quit', self)
        # self.btn_quit.move(190, 10)
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit) 

        self.btn3 = QPushButton("樣本數")
        self.count_edit = QLineEdit("1")
        self.btn3.clicked.connect(self.getInt)

        # self.v_layout = QHBoxLayout()
        # self.v_layout.addWidget(self.plt)
        # self.v_layout.addWidget(self.btn3,0,Qt.AlignBottom | Qt.AlignLeft)
        # self.v_layout.addWidget(self.count_edit)
        # self.v_layout.addWidget(self.btn_start)
        # self.v_layout.addWidget(self.btn_stop)
        # self.v_layout.addWidget(self.btn_quit) 
        # self.setLayout(self.v_layout)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.plt, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.btn3,1, 0)
        self.gridLayout.addWidget(self.count_edit,1, 1)
        self.gridLayout.addWidget(self.btn_start,2, 0)
        self.gridLayout.addWidget(self.btn_stop,3, 0)
        self.gridLayout.addWidget(self.btn_quit,4, 0) 
        self.setLayout(self.gridLayout)

    def drawLine(self):
        # if(self.series.count()>2000):
        #     self.series.removePoints(0,self.series.count()-5000)
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

            line_1 = self.plt.plot(
                data_list, 
                pen='r', 
                symbol='o', 
                symbolPen='b', 
                symbolBrush='w', 
                name= str(len(data_list)) + " : " + str(data)
            ) 
            line_2 = self.plt.plot(
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
        #2秒觸發一次，更新數據
        self.timer.start(1000)

    def stop_timer(self):
        #停止更新數據
        self.timer.stop()

    def getInt(self):
        num,ok = QInputDialog.getInt(self, "Text Input Dialog", "輸入數字")
        if ok:
            self.count_edit.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())