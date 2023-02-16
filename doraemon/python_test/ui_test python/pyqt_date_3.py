import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtChart import QDateTimeAxis,QValueAxis,QChart,QChartView, QLineSeries
from PyQt5.QtWidgets import QApplication,QPushButton, QGraphicsScene, QGraphicsView, QLineEdit, QInputDialog, QMessageBox
from PyQt5.QtGui import QPainter, QFont 
from PyQt5.QtCore import QDateTime,Qt,QTimer
from pyModbusTCP.client import ModbusClient


class ChartView(QChartView,QChart):
    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        
        # 畫面放大縮小
        self.isTouching = False 
        self.setRubberBand(QChartView.RectangleRubberBand)
        self.resize(1400, 800)

        self._scene = QGraphicsScene(self)
        self._view = QGraphicsView(self._scene)

        self.setRenderHint(QPainter.Antialiasing)  # 抗鋸齒
        self.chart_init()
        
        # Time init
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        
        # Start bottom
        self.btn_start = QPushButton('Start', self)
        self.btn_start.move(10, 10)
        self.btn_start.clicked.connect(self.start_timer)

        # Stop bottom
        self.btn_stop = QPushButton('Stop', self)
        self.btn_stop.move(100, 10)
        self.btn_stop.clicked.connect(self.stop_timer)

        # Clean bottom
        self.btn_clean = QPushButton('Clean', self)
        self.btn_clean.move(190, 10)
        self.btn_clean.clicked.connect(self.cleanPlot) 

        # 取樣頻率
        self.btn_speed = QPushButton('Speed Millisecond', self)
        self.btn_speed.move(280, 10)
        self.speed_edit = QLineEdit("1000", self)
        self.speed_edit.move(415, 10)
        self.btn_speed.clicked.connect(self.getTime)

        # IP address
        self.btn_ip = QPushButton("IP", self)
        self.btn_ip.move(570, 10)
        self.ip_edit = QLineEdit('127.0.0.1', self)
        self.ip_edit.move(655, 10)
        self.btn_ip.clicked.connect(self.getIP)

        # Port
        self.btn_port = QPushButton("Port", self)
        self.btn_port.move(810, 10)
        self.port_edit = QLineEdit("502", self)
        self.port_edit.move(895, 10)
        self.btn_port.clicked.connect(self.getPort)

        self.btn_quit = QPushButton('Quit', self)
        self.btn_quit.move(1080, 10)
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)

    def start_timer(self):
        # 更新數據取樣頻率
        if self.speed_edit:
            self.timer.start(int(self.speed_edit.text()))
        else:
            self.timer.start(1000)

    def stop_timer(self):
        # 停止更新數據
        self.timer.stop()

    def getIP(self):
        # IP Address
        ip,ok = QInputDialog.getText(self, "Text Input IP", "輸入IP")
        if ok:
            self.ip_edit.setText(str(ip))

    def getPort(self):
        # Port
        port,ok = QInputDialog.getInt(self, "Text Input Port", "輸入Port")
        if ok:
            self.port_edit.setText(str(port))

    def getTime(self):
        # 資料取樣時間
        time,ok = QInputDialog.getInt(self, "Text Input Time", "輸入取樣時間")
        if ok:
            self.time_edit.setText(str(time))

    def cleanPlot(self):
        self.series.clear()

    def chart_init(self):
        self.chart = QChart()
        self.series = QLineSeries()
        
        # 點標籤字體
        self.series.setPointLabelsFont(QFont("微軟雅黑"))

        # 顯示點位數值
        self.series.setPointLabelsFormat("@yPoint")

        # 點標籤是否可視
        self.series.setPointLabelsVisible(True)

        # 設置點標籤是否可視
        self.series.setPointsVisible(True)

        # 是否切割邊緣點標籤
        self.series.setPointLabelsClipping(True)

        # 設定曲線名稱
        self.series.setName("即時曲線")
        
        # 把曲線添加到QChart中
        self.chart.addSeries(self.series)
        
        # 初始化 X 軸，Y 軸
        self.dtaxisX = QDateTimeAxis()
        self.vlaxisY = QValueAxis()
        
        # 設定座標顯示範圍
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-10*1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(300)
        
        # 設定 X 軸時間樣式
        self.dtaxisX.setFormat("MM月dd hh:mm:ss")
        
        # 設定座標軸上格點
        self.dtaxisX.setTickCount(10)
        self.vlaxisY.setTickCount(20)
        
        # 設定座標軸名稱
        self.dtaxisX.setTitleText("時間")
        self.vlaxisY.setTitleText("數值")
        
        # 設定網格不顯示
        # self.vlaxisY.setGridLineVisible(False)
        self.vlaxisY.setGridLineVisible(True)
        
        # 座標軸添加到 chart 中
        self.chart.addAxis(self.dtaxisX,Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY,Qt.AlignLeft)
        
        # 把曲線關聯到坐標軸
        self.series.attachAxis(self.dtaxisX)
        self.series.attachAxis(self.vlaxisY)

        self.setChart(self.chart)

    def keyPressEvent(self, event):        
        if event.key() == Qt.Key_Plus:            
            self.chart().zoomIn()        
        elif event.key() == Qt.Key_Minus:            
            self.chart().zoomOut()        
        elif event.key() == Qt.Key_Left:            
            self.chart().scroll(-10, 0)        
        elif event.key() == Qt.Key_Right:            
            self.chart().scroll(10, 0)        
        elif event.key() == Qt.Key_Up:            
            self.chart().scroll(0, 10)        
        elif event.key() == Qt.Key_Down:            
            self.chart().scroll(0, -10)       
        else:            
            QGraphicsView.keyPressEvent(self, event)

    def drawLine(self):
        # 獲取當前時間
        bjtime = QDateTime.currentDateTime()
        
        # 更新 X 軸座標
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-100*1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        
        # 當曲線上的點超出 X 軸的範圍時， 移除最早的點
        if(self.series.count()>2000):
            self.series.removePoints(0,self.series.count()-5000)
        
        # 接收 modbus server 資料
        HOST = self.ip_edit.text()
        PORT = int(self.port_edit.text())

        c1 = ModbusClient()
        c1.host(HOST)
        c1.port(PORT)
        c1.unit_id(1)

        if not c1.is_open():
            if not c1.open():
                # 通訊失敗, 顯示錯誤視窗
                replay = QMessageBox.information(self, '錯誤', "unable to connect to "+HOST+":"+str(PORT), QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok) 
                if replay == QMessageBox.Ok or replay == QMessageBox.Cancel:
                    self.timer.stop()
                    QMessageBox.done(1)

        if c1.is_open():
            # read 2 registers at address 0, store result in regs list
            regs = c1.read_holding_registers(0, 50)
            yint = regs[39]

        # 添加數據到曲線末端
        self.series.append(bjtime.toMSecsSinceEpoch(),yint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.show()
    sys.exit(app.exec_())