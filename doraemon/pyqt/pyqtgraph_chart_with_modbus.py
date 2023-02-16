import sys
import pyqtgraph as pg 

from pyModbusTCP.client import ModbusClient
from PyQt5.QtCore import Qt, QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QGridLayout, QLabel


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

        #clean bottom
        self.btn_clean = QPushButton('Clean', self)
        self.btn_clean.clicked.connect(self.cleanPlot) 

        #sample_count bottom
        self.btn_sample_count = QPushButton("樣本數")
        self.count_edit = QLineEdit("1")
        self.btn_sample_count.clicked.connect(self.getCount)

        #time bottom
        self.btn_time = QPushButton("取樣時間")
        self.time_edit = QLineEdit("1000")
        self.btn_time.clicked.connect(self.getTime)

        #ip address
        self.btn_ip = QPushButton("設備 IP")
        self.ip_edit = QLineEdit("127.0.0.1")
        self.btn_ip.clicked.connect(self.getIP)

        #port
        self.btn_port = QPushButton("設備 Port")
        self.port_edit = QLineEdit("502")
        self.btn_port.clicked.connect(self.getPort)

        #grid_layout
        self.gridLayout = QGridLayout(self)

        #grid address
        #addWidget(*row, *column, *use_row, *use_column)
        #Add Plot
        self.gridLayout.addWidget(self.plt, 0, 0, 1, 2)
        
        #Add IP
        self.gridLayout.addWidget(self.btn_ip, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.ip_edit,1, 1, 1, 1)

        #Add Port
        self.gridLayout.addWidget(self.btn_port, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.port_edit,2, 1, 1, 1)   

        #Add Sample Count
        self.gridLayout.addWidget(self.btn_sample_count, 3, 0)
        self.gridLayout.addWidget(self.count_edit, 3, 1)

        #Add Bottom
        self.gridLayout.addWidget(self.btn_time, 4, 0)
        self.gridLayout.addWidget(self.time_edit, 4, 1)
        self.gridLayout.addWidget(self.btn_start, 5, 0)
        self.gridLayout.addWidget(self.btn_stop, 5, 1)
        self.gridLayout.addWidget(self.btn_quit, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_clean, 6, 1, 1, 2) 
        self.gridLayout.addWidget(self.lab2, 7, 0)
        self.setLayout(self.gridLayout)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # print(type(event.pos().x()))    #<class 'int'>
            self.lab2.setText(str(event.pos().x())+","+str(event.pos().y()))
        # self.pos = event.pos()
        # print(self.pos)
        # self.lab2.setText(str(event.pos().x()) + "," + str(event.pos().y()))
        # self.update()

    def drawLine(self):
        HOST = self.ip_edit.text()
        PORT = int(self.port_edit.text())

        c1 = ModbusClient()
        c1.host(HOST)
        c1.port(PORT)
        c1.unit_id(1)
        
        data_list = []
        data_list_1 = []
        
        #接收 modbus server 資料
        if not c1.is_open():
            if not c1.open():
                print("unable to connect to "+HOST+":"+str(PORT))

        if c1.is_open():
            # read 2 registers at address 0, store result in regs list
            regs = c1.read_holding_registers(0, 5)
            data = regs[0]
            data_1 = regs[1]

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
                symbol='star', 
                symbolPen='b', 
                symbolBrush='w', 
                name= str(len(data_list_1)) + " : " + str(data_1)
            )

        if len(data_list) == int(self.count_edit.text()):
            data_list = []
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

    def getCount(self):
        #資料取樣數
        num,ok = QInputDialog.getInt(self, "Text Input Dialog", "輸入取樣數")
        if ok:
            self.count_edit.setText(str(num))

    def getTime(self):
        #資料取樣時間
        time,ok = QInputDialog.getInt(self, "Text Input Time", "輸入取樣時間")
        if ok:
            self.time_edit.setText(str(time))

    def getIP(self):
        #IP Address
        ip,ok = QInputDialog.getText(self, "Text Input IP", "輸入IP")
        if ok:
            self.ip_edit.setText(str(ip))

    def getPort(self):
        #Port
        port,ok = QInputDialog.getInt(self, "Text Input Port", "輸入Port")
        if ok:
            self.port_edit.setText(str(port))

    def cleanPlot(self):
        self.plt.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())