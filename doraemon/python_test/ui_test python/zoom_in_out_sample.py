# https://blog.csdn.net/weixin_42509833/article/details/113709490

import sys,math 
from PyQt5.QtCore import Qt, QTimer, QRandomGenerator, QEvent, QPointF
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt5.QtChart import QChart, QChartView,QLineSeries, QValueAxis   
class MyChartView(QChartView):    
    def __init__(self, chart, parent = None):        
        super(MyChartView, self).__init__(chart, parent)        
        self.isTouching = False        
        self.setRubberBand(QChartView.RectangleRubberBand)               
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
class DemoZoomLineChart(QMainWindow):    
    def __init__(self, parent=None):        
        super(DemoZoomLineChart, self).__init__(parent)                    
        # 设置窗口标题        
        self.setWindowTitle('实战 Qt for Python: 线条缩放演示')              
        # 设置窗口大小        
        self.resize(480, 360)                
        self.createChart()        
    def createChart(self):        
        series = QLineSeries()        
        for i in range(50):            
            pnt = QPointF(i, math.sin(math.pi * i / 50) * 100 + QRandomGenerator.global_().bounded(20))            
            series.append(pnt)                
        chart = QChart()        
        chart.setTitle('线条缩放显示')        
        chart.addSeries(series)     
        chart.setAnimationOptions(QChart.SeriesAnimations)        
        chart.legend().hide()       
        chart.createDefaultAxes()                
        chartView =MyChartView(chart)        
        chartView.setRenderHint(QPainter.Antialiasing)        
        self.setCentralWidget(chartView)      
if __name__ == '__main__':    
    app = QApplication(sys.argv)    
    window = DemoZoomLineChart()    
    window.show()    
    sys.exit(app.exec())   