import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5 import QtCore, QtGui

class MainWindow(QMainWindow):
    class ChartView(QChartView):
        def __init__(self, chart):
            super().__init__(chart)        

        mouseMoved = QtCore.pyqtSignal(QtCore.QPoint)

        def mouseMoveEvent(self, event):
            self.mouseMoved.emit(event.pos())

            return QChartView.mouseMoveEvent(self, event)

    class Chart(QChart):
        def __init__(self):
            super().__init__()

        def mouseMoveEvent(self, event):
            print("Chart.mouseMoveEvent", event.pos().x(), event.pos().y())

            return QChart.mouseMoveEvent(self, event)

    def __init__(self, args):
        super().__init__()

        chartView = self.ChartView(self.Chart())
        chartView.setRenderHint(QtGui.QPainter.Antialiasing)
        chartView.setRubberBand(QChartView.HorizontalRubberBand)

        chartView.chart().createDefaultAxes()
        chartView.chart().legend().hide()
        chartView.chart().addAxis(QValueAxis(), QtCore.Qt.AlignBottom)
        chartView.chart().addAxis(QValueAxis(), QtCore.Qt.AlignLeft)

        ls = QLineSeries()
        ls.append(0, 0)
        ls.append(9, 9)
        ls.attachAxis(chartView.chart().axisX())
        ls.attachAxis(chartView.chart().axisY())
        chartView.chart().addSeries(ls)

        self.setCentralWidget(chartView)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow(sys.argv)
    sys.exit(app.exec_())