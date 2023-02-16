import adafruit_amg88xx
import busio
import board
import os
import sys
import time
import pygame
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication,  QFrame, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont



i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)
temp_data = 0

class window(QWidget):
    def __init__(self):
        super().__init__()

        # Sub Window
        self.sub_window = SubWindow()
        self.timer = QTimer()

        self.normal = 0
        self.alarm = 0
        
        pygame.mixer.init()

        # Temperature title box
        self.temp_title = QLabel(self)
        self.temp_title.setText('<font color=%s>%s</font>'%('#00CED1', '檢測溫度 : '))
        self.temp_title.setFrameShape(QFrame.Box)
        self.temp_title.setFrameShadow(QFrame.Raised)
        self.temp_title.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.temp_title.setAlignment(Qt.AlignTop)
        self.temp_title.setGeometry(250,10,730,330) # (水平, 垂直, 寬度, 高度)

        # Temperature unit box
        self.unit = QLabel(self)
        self.unit.setText('<font color=%s>%s</font>'%('#00CED1', '°C'))
        self.unit.setGeometry(780,120,180,200) # (水平, 垂直, 寬度, 高度)

        # Temperature
        self.temp_show = QLabel(self)
        self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', '0.00'))
        self.temp_show.setGeometry(350,120,430,200) # (水平, 垂直, 寬度, 高度)

        # Title with number of people measured box
        self.title_with_number_of_people_measured = QLabel(self)
        self.title_with_number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', '測溫人數 : '))
        self.title_with_number_of_people_measured.setFrameShape(QFrame.Box)
        self.title_with_number_of_people_measured.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_people_measured.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.title_with_number_of_people_measured.setAlignment(Qt.AlignTop)
        self.title_with_number_of_people_measured.setGeometry(10,10,220,160) 

        # Number of people measured box
        self.number_of_people_measured = QLabel(self)
        self.number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', '0'))
        self.number_of_people_measured.setGeometry(30,80,180,70) 

        # Title with number of alarm box
        self.title_with_number_of_alarm = QLabel(self)
        self.title_with_number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', '報警次數 : '))
        self.title_with_number_of_alarm.setFrameShape(QFrame.Box)
        self.title_with_number_of_alarm.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_alarm.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.title_with_number_of_alarm.setAlignment(Qt.AlignTop)
        self.title_with_number_of_alarm.setGeometry(10,180,220,160)

        # Number of alarm
        self.number_of_alarm = QLabel(self)
        self.number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', '0'))
        self.number_of_alarm.setGeometry(30,260,180,70) 

        # Setting normal & alarm temp bottom
        self.btn_setting_with_temp_upper_and_lower_limits = QPushButton('設定', self)
        self.btn_setting_with_temp_upper_and_lower_limits.setStyleSheet('color: darkturquoise')
        self.btn_setting_with_temp_upper_and_lower_limits.clicked.connect(self.sub_window.show) 
        self.btn_setting_with_temp_upper_and_lower_limits.setGeometry(990,10,200,100)

        # Scan box
        self.scan = QLabel(self)
        self.scan.setText('量測中.....')
        self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中.....'))
        self.scan.setFrameShape(QFrame.Box)
        self.scan.setFrameShadow(QFrame.Raised)
        self.scan.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.scan.setAlignment(Qt.AlignCenter)
        self.scan.setGeometry(990,120,200,220)  

        # Clean bottom
        self.btn_clean = QPushButton('清零', self)
        self.btn_clean.setStyleSheet('color: darkturquoise')
        self.btn_clean.clicked.connect(self.clean) 
        self.btn_clean.setGeometry(10,360,220,130)

        # Announcement box
        self.announcement = QLabel(self)
        self.announcement.setText('<font color=%s>%s</font>'%('#00CED1', '請保持 1 米距離, 戴口罩, 勤洗手!!'))
        self.announcement.setFrameShape(QFrame.Box)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.announcement.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.announcement.setAlignment(Qt.AlignCenter)
        self.announcement.setGeometry(250,360,940,130) 

        # 設訂字體及大小
        self.temp_title.setFont(QFont("Roman times",30,QFont.Bold))
        self.temp_show.setFont(QFont("Roman times",100,QFont.Bold))
        self.unit.setFont(QFont("Roman times",100,QFont.Bold))
        self.title_with_number_of_people_measured.setFont(QFont("Roman times",30,QFont.Bold))
        self.number_of_people_measured.setFont(QFont("Roman times",30,QFont.Bold))
        self.title_with_number_of_alarm.setFont(QFont("Roman times",30,QFont.Bold))
        self.number_of_alarm.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_clean.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_setting_with_temp_upper_and_lower_limits.setFont(QFont("Roman times",30,QFont.Bold))
        self.announcement.setFont(QFont("Roman times",30,QFont.Bold))
        self.scan.setFont(QFont("Roman times",30,QFont.Bold))

        # Windows show address
        self.setGeometry(500,200,1200,500) # 視窗顯示位置
        self.setStyleSheet('background-color:black')
        
        # Windows title name
        self.setWindowTitle("溫度監測")

        self.timer.timeout.connect(self.get_temp_data)
        self.timer.start(2000)

    def clean(self):
        self.init_count = 0
        self.number_of_people_measured.setText(str(self.init_count))
        self.number_of_alarm.setText(str(self.init_count))

    def get_temp_data(self):
        temp_data = 0
        self.row_list = []
        
        for row in amg.pixels:
            for temp in row:
                self.row_list.append(temp)
                if len(self.row_list) == 64:
                    temp_data = max(self.row_list)
                    self.row_list.clear()      
        
        if temp_data > 35:
            self.temp_show.setText(str(temp_data))
            self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', str(temp_data)))
        
        normal_temp_text = self.sub_window.normal_temp_edit.text()
        if normal_temp_text:
            normal_temp = float(normal_temp_text)
        else:
            normal_temp = 0.0

        alarm_temp_text = self.sub_window.alarm_temp_edit.text()
        if alarm_temp_text:
            alarm_temp = float(alarm_temp_text)
        else:
            alarm_temp = 0.0


        if ( normal_temp == 0.0 and alarm_temp == 0.0 ):
            self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中.....'))
            self.normal = 0
            self.alarm = 0
        elif (temp_data >= normal_temp and temp_data <= alarm_temp) :
            self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '溫度正常 \n, 請通過 \n'))
            pygame.mixer.music.load('/home/pi/safe.mp3')
            pygame.mixer.music.play()
            self.normal += 1
        elif temp_data >= alarm_temp and alarm_temp > 36:
            self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '溫度異常 \n, 請留步 \n'))
            pygame.mixer.music.load('/home/pi/alarm.mp3')
            pygame.mixer.music.play()
            self.alarm += 1
            self.normal += 1
        else:
            time.sleep(5)
            self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中.....'))
            self.alarm += 0
            self.normal += 0
            self.temp_show.setText(str(0.00))
        self.number_of_alarm.setText(str(self.alarm))
        self.number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', str(self.alarm)))
        self.number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', str(self.normal)))


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.normal_temp_title = QLabel(self)
        self.normal_temp_title.setText('設置正常溫度值 :             °C  ')
        self.normal_temp_title.setGeometry(250,150,1000,100) # (水平, 垂直, 寬度, 高度)

        self.normal_temp_edit = QLineEdit(self)
        self.normal_temp_edit.setText('0.00')
        self.normal_temp_edit.setGeometry(680,150,200,100) 

        self.alarm_temp_title = QLabel(self)
        self.alarm_temp_title.setText('設置報警溫度值 :             °C  ')
        self.alarm_temp_title.setGeometry(250,300,1000,100) # (水平, 垂直, 寬度, 高度)

        self.alarm_temp_edit = QLineEdit(self)
        self.alarm_temp_edit.setText('0.00')
        self.alarm_temp_edit.setGeometry(680,300,200,100) 

        self.btn_finish = QPushButton('確定', self)
        self.btn_finish.clicked.connect(self.close)
        self.btn_finish.setGeometry(500,430,200,100) 

        self.normal_temp_title.setFont(QFont("Roman times",40,QFont.Bold))
        self.normal_temp_edit.setFont(QFont("Roman times",40,QFont.Bold))
        self.alarm_temp_title.setFont(QFont("Roman times",40,QFont.Bold))
        self.alarm_temp_edit.setFont(QFont("Roman times",40,QFont.Bold))
        self.btn_finish.setFont(QFont("Roman times",40,QFont.Bold))

        self.setGeometry(500,300,1200,600) # 視窗顯示位置
        self.setWindowTitle("溫度設定")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_()) 