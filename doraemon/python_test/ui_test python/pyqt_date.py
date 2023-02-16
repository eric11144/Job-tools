import sys
import random
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtChart import QDateTimeAxis,QValueAxis,QSplineSeries,QChart,QChartView
from PyQt5.QtWidgets import QApplication,QPushButton, QShortcut, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPainter, QKeySequence
from PyQt5.QtCore import QDateTime,Qt,QTimer
from pyModbusTCP.client import ModbusClient


HOST1 = "127.0.0.1"
PORT1 = 502
c1 = ModbusClient()
c1.host(HOST1)
c1.port(PORT1)
c1.unit_id(1)

class ChartView(QChartView,QChart):
    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)

        self._scene = QGraphicsScene(self)
        self._view = QGraphicsView(self._scene)

        self.setRenderHint(QPainter.Antialiasing)  # 抗鋸齒
        self.chart_init()
        #Time init
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        #bottom
        btn_start = QPushButton('Start', self)
        btn_start.move(10, 10)
        btn_start.clicked.connect(self.start_timer)

        btn_stop = QPushButton('Stop', self)
        btn_stop.move(100, 10)
        btn_stop.clicked.connect(self.stop_timer)

        btn_quit = QPushButton('Quit', self)
        btn_quit.move(190, 10)
        btn_quit.clicked.connect(QCoreApplication.instance().quit)


    def start_timer(self):
        #2秒觸發一次，更新數據
        self.timer.start(1000)

    def stop_timer(self):
        #停止更新數據
        self.timer.stop()

    def chart_init(self):
        self.chart = QChart()
        self.series = QSplineSeries()

        #設定曲線名稱
        self.series.setName("即時曲線")
        #把曲線添加到QChart中
        self.chart.addSeries(self.series)
        #初始化X軸，Y軸
        self.dtaxisX = QDateTimeAxis()
        self.vlaxisY = QValueAxis()
        #設定座標顯示範圍
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-10*1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(30)
        #設定 X 軸時間樣式
        self.dtaxisX.setFormat("MM月dd hh:mm:ss")
        #設定座標軸上格點
        self.dtaxisX.setTickCount(3)
        self.vlaxisY.setTickCount(11)
        #設定座標軸名稱
        self.dtaxisX.setTitleText("時間")
        self.vlaxisY.setTitleText("數值")
        #設定網格不顯示
        self.vlaxisY.setGridLineVisible(False)
        #座標軸添加到chart中
        self.chart.addAxis(self.dtaxisX,Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY,Qt.AlignLeft)
        #把曲線關聯到坐標軸
        self.series.attachAxis(self.dtaxisX)
        self.series.attachAxis(self.vlaxisY)

        self.setChart(self.chart)
    def drawLine(self):
        #獲取當前時間
        bjtime = QDateTime.currentDateTime()
        #更新X軸座標
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-100*1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        #當曲線上的點超出X軸的範圍時，移除最早的點
        if(self.series.count()>2000):
            self.series.removePoints(0,self.series.count()-5000)
        #接收 modbus server 資料
        if not c1.is_open():
            if not c1.open():
                print("unable to connect to "+HOST1+":"+str(PORT1))

        if c1.is_open():
            # read 2 registers at address 0, store result in regs list
            regs = c1.read_holding_registers(0, 50)
            yint = regs[39]
        # yint = random.randint(0,1500)
        # QPainter.setPen(Qt.red)
        # qp = QPainter()
        # a = int(bjtime.toSecsSinceEpoch() / 1000)
        # qp.drawPoint(yint, yint)
        # print(type(bjtime.toMSecsSinceEpoch()))
        #添加數據到曲線末端
        self.series.append(bjtime.toMSecsSinceEpoch(),yint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.show()
    sys.exit(app.exec_())