import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QComboBox
from PyQt5.QtGui import QFont


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.sub_window = SubWindow()

        self.btn_setting_with_caffeamericano = QPushButton('美式咖啡', self)
        self.btn_setting_with_caffeamericano.setStyleSheet('border-width: 2px; border-style: solid; border-image: url(caffeamericano.png); border-color:rgb(193, 205, 205); color: darkturquoise')
        self.btn_setting_with_caffeamericano.clicked.connect(self.sub_window.show) 
        self.btn_setting_with_caffeamericano.setGeometry(0,10,300,400)

        self.btn_setting_with_latte = QPushButton('拿鐵', self)
        self.btn_setting_with_latte.setStyleSheet('border-width: 2px; border-style: solid; border-image: url(latte.png); border-color:rgb(193, 205, 205); color: darkturquoise')
        self.btn_setting_with_latte.clicked.connect(self.sub_window.show) 
        self.btn_setting_with_latte.setGeometry(400,10,300,400)

        self.btn_setting_with_cappuccino = QPushButton('卡布其諾', self)
        self.btn_setting_with_cappuccino.setStyleSheet('border-width: 2px; border-style: solid; border-image: url(cappuccino.png); border-color:rgb(193, 205, 205); color: darkturquoise')
        self.btn_setting_with_cappuccino.clicked.connect(self.sub_window.show) 
        self.btn_setting_with_cappuccino.setGeometry(800,10,300,400)

        self.btn_setting_with_caffeamericano.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_setting_with_latte.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_setting_with_cappuccino.setFont(QFont("Roman times",30,QFont.Bold))

        # Windows show address
        self.setGeometry(500,200,1200,500) # 視窗顯示位置
        self.setStyleSheet('background-color:white')
        
        # Windows title name
        self.setWindowTitle("點餐系統")

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sugar_title = QLabel(self)
        self.sugar_title.setText('甜度 : ')
        self.sugar_title.setGeometry(250,150,1000,100) # (水平, 垂直, 寬度, 高度)

        self.sugar_combobox = QComboBox(self)
        self.sugar_combobox.addItems(['無糖', '微糖', '半糖', '全糖'])
        self.sugar_combobox.setGeometry(680,150,200,100) 

        self.temp_title = QLabel(self)
        self.temp_title.setText('溫度 : ')
        self.temp_title.setGeometry(250,300,1000,100) # (水平, 垂直, 寬度, 高度)

        self.temp_combobox = QComboBox(self)
        self.temp_combobox.addItems(['熱', '常溫', '微冰', '少冰', '全冰'])
        self.temp_combobox.setGeometry(680,300,200,100) 

        self.btn_finish = QPushButton('確定', self)
        self.btn_finish.clicked.connect(self.close)
        self.btn_finish.setGeometry(500,430,200,100) 

        self.sugar_title.setFont(QFont("Roman times",40,QFont.Bold))
        self.sugar_combobox.setFont(QFont("Roman times",40,QFont.Bold))
        self.temp_title.setFont(QFont("Roman times",40,QFont.Bold))
        self.temp_combobox.setFont(QFont("Roman times",40,QFont.Bold))
        self.btn_finish.setFont(QFont("Roman times",40,QFont.Bold))

        self.setGeometry(500,300,1200,600) # 視窗顯示位置
        self.setWindowTitle("溫度甜度選擇")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_()) 
