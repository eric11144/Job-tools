import adafruit_amg88xx
import ast
import busio
import board
import os
import digitalio
import simpleaudio
import sys
import time
from micropython import const
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication,  QFrame, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont
from smbus import SMBus


i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c, addr=0x69)

bus = SMBus(1)
addr = const(0x52)


class window(QWidget):
    def __init__(self):
        super().__init__()
        
        # Sub Window
        self.sub_window = SubWindow()
        self.timer = QTimer()

        self.normal = 0
        self.alarm = 0
        self.status = 0
        self.count = 0

        # Temperature title box
        self.temp_title = QLabel(self)
        self.temp_title.setText('<font color=%s>%s</font>'%('#00CED1', '檢測溫度 : '))
        self.temp_title.setFrameShape(QFrame.Box)
        self.temp_title.setFrameShadow(QFrame.Raised)
        self.temp_title.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.temp_title.setAlignment(Qt.AlignTop)
        self.temp_title.setGeometry(610,10,1000,640) # (水平, 垂直, 寬度, 高度)

        # Temperature unit box
        self.unit = QLabel(self)
        self.unit.setText('<font color=%s>%s</font>'%('#00CED1', '°C'))
        self.unit.setGeometry(1340,220,500,400) # (水平, 垂直, 寬度, 高度)

        # Temperature
        self.temp_show = QLabel(self)
        self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', '0.00'))
        self.temp_show.setGeometry(670,220,670,390) # (水平, 垂直, 寬度, 高度)

        # Title with number of people measured box
        self.title_with_number_of_people_measured = QLabel(self)
        self.title_with_number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', '測溫人數 : '))
        self.title_with_number_of_people_measured.setFrameShape(QFrame.Box)
        self.title_with_number_of_people_measured.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_people_measured.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.title_with_number_of_people_measured.setAlignment(Qt.AlignTop)
        self.title_with_number_of_people_measured.setGeometry(10,10,600,320) 

        # Number of people measured box
        self.number_of_people_measured = QLabel(self)
        self.number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', '0'))
        self.number_of_people_measured.setGeometry(50,180,360,140) 

        # Title with number of alarm box
        self.title_with_number_of_alarm = QLabel(self)
        self.title_with_number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', '報警次數 : '))
        self.title_with_number_of_alarm.setFrameShape(QFrame.Box)
        self.title_with_number_of_alarm.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_alarm.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.title_with_number_of_alarm.setAlignment(Qt.AlignTop)
        self.title_with_number_of_alarm.setGeometry(10,330,600,320)

        # Number of alarm
        self.number_of_alarm = QLabel(self)
        self.number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', '0'))
        self.number_of_alarm.setGeometry(50,500,360,140) 

        # Setting normal & alarm temp bottom
        self.btn_setting_with_temp_upper_and_lower_limits = QPushButton('設定', self)
        self.btn_setting_with_temp_upper_and_lower_limits.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205); color: darkturquoise')
        self.btn_setting_with_temp_upper_and_lower_limits.clicked.connect(self.sub_window.showFullScreen) 
        self.btn_setting_with_temp_upper_and_lower_limits.setGeometry(1600,10,300,200)

        # Scan box
        self.scan = QLabel(self)
        self.scan.setText('量測中...')
        self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中...'))
        self.scan.setWordWrap(True)
        self.scan.setFrameShape(QFrame.Box)
        self.scan.setFrameShadow(QFrame.Raised)
        self.scan.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.scan.setAlignment(Qt.AlignCenter)
        self.scan.setGeometry(1600,210,300,440)  

        # Clean bottom
        self.btn_clean = QPushButton('清零', self)
        self.btn_clean.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205); color: darkturquoise')
        self.btn_clean.clicked.connect(self.clean) 
        self.btn_clean.setGeometry(10,650,320,400)

        # Announcement box
        self.announcement = QLabel(self)
        self.announcement.setText('<font color=%s>%s</font>'%('#00CED1', '請保持 1 米距離, 戴口罩, 勤洗手!!'))
        self.announcement.setFrameShape(QFrame.Box)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.announcement.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(193, 205, 205)')
        self.announcement.setAlignment(Qt.AlignCenter)
        self.announcement.setGeometry(330,650,1570,400) 

        # 設訂字體及大小
        self.temp_title.setFont(QFont("Roman times",80,QFont.Bold))
        self.temp_show.setFont(QFont("Roman times",160,QFont.Bold))
        self.unit.setFont(QFont("Roman times",150,QFont.Bold))
        self.title_with_number_of_people_measured.setFont(QFont("Roman times",80,QFont.Bold))
        self.number_of_people_measured.setFont(QFont("Roman times",80,QFont.Bold))
        self.title_with_number_of_alarm.setFont(QFont("Roman times",80,QFont.Bold))
        self.number_of_alarm.setFont(QFont("Roman times",80,QFont.Bold))
        self.btn_clean.setFont(QFont("Roman times",80,QFont.Bold))
        self.btn_setting_with_temp_upper_and_lower_limits.setFont(QFont("Roman times",80,QFont.Bold))
        self.announcement.setFont(QFont("Roman times",70,QFont.Bold))
        self.scan.setFont(QFont("Roman times",40,QFont.Bold))

        # Windows show address
        self.setGeometry(1024,600,1200,500) # 視窗顯示位置
        self.setStyleSheet('background-color:black')
        
        # Windows title name
        self.setWindowTitle("溫度監測")
        
        self.timer.timeout.connect(self.get_temp_data)
        self.timer.start(500)

    def clean(self):
        self.normal = 0
        self.alarm = 0
        self.number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', str(self.normal)))
        self.number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', str(self.alarm)))

    def range_mm(self):
        bus.write_byte(addr,0)
        time.sleep(0.02)
        value = bus.read_byte(addr) << 8 | bus.read_byte(addr)
        time.sleep(0.01)
        return value

    def get_temp_data(self):
        temp_data = 0
        temp_average = 0
        distance = self.range_mm()
        self.row_list = []
        print(distance)
        
        if distance < 200:
            for row in amg.pixels:
                for temp in row:
                    self.row_list.append(round(temp,1))
                    if len(self.row_list) == 64:
                        temp_data = max(self.row_list)
                        temp_average = round((sum(self.row_list) / 64),1)
                        self.row_list.clear()      

            if temp_data > temp_average and temp_data < 30:
                temp_data += 9.7
            
            normal_temp_text = self.sub_window.normal_temp_edit.text()
            
            try:
                normal_temp = float(normal_temp_text)
            except ValueError:
                normal_temp = 0.0

            alarm_temp_text = self.sub_window.alarm_temp_edit.text()
            
            try:
                alarm_temp = float(alarm_temp_text)
            except ValueError:
                alarm_temp = 0.0


            if ( normal_temp == 0.0 and alarm_temp == 0.0 ):
                self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中...'))
                self.normal = 0
                self.alarm = 0
            elif ( temp_data >= normal_temp and temp_data <= alarm_temp ) :
                self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '溫度正常,請通過'))
                output = digitalio.DigitalInOut(board.D17)
                output.direction = digitalio.Direction.OUTPUT
                output.value = True
                output.value = False
                self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', str(temp_data)))
                if (self.status != 1):
                    wave_obj = simpleaudio.WaveObject.from_wave_file("/home/pi/ok.wav")
                    wave_obj.play()
                    self.status = 1
                    self.normal += 1
            elif ( temp_data >= alarm_temp ):
                self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '溫度異常,請留步'))
                output = digitalio.DigitalInOut(board.D27)
                output.direction = digitalio.Direction.OUTPUT
                output.value = True
                output.value = False
                self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', str(temp_data)))
                if (self.status != 2):
                    wave_obj = simpleaudio.WaveObject.from_wave_file("/home/pi/error.wav")
                    wave_obj.play()
                    self.status = 2
                    self.alarm += 1
                    self.normal += 1
            elif ( self.count == 20 ):
                self.scan.setText('<font color=%s>%s</font>'%('#00CED1', '量測中...'))
                self.alarm += 0
                self.normal += 0
                self.count = 0
                self.status = 0
                self.temp_show.setText('<font color=%s>%s</font>'%('#00CED1', str(0.0)))
            else:
                self.count += 1
                
            self.number_of_alarm.setText('<font color=%s>%s</font>'%('#00CED1', str(self.alarm)))
            self.number_of_people_measured.setText('<font color=%s>%s</font>'%('#00CED1', str(self.normal)))


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.filepath = '/home/pi/temp.txt'

        with open(self.filepath, 'r') as output: 
            data = output.read()
            self.temp_dict = ast.literal_eval(data)
            self.normal_temp_setting = self.temp_dict['normal_temp_setting']
            self.alarm_temp_setting = self.temp_dict['alarm_temp_setting']

        self.normal_temp_title = QLabel(self)
        self.normal_temp_title.setText('設置正常溫度值 :             °C  ')
        self.normal_temp_title.setGeometry(250,400,1230,100) # (水平, 垂直, 寬度, 高度)

        self.normal_temp_add = QPushButton('+', self)
        self.normal_temp_add.clicked.connect(self.normal_temp_control_add)
        self.normal_temp_add.setGeometry(1550,400,100,100) 

        self.normal_temp_edit = QLineEdit(self)
        self.normal_temp_edit.setText(str(self.normal_temp_setting))
        self.normal_temp_edit.setGeometry(950,400,200,100) 

        self.normal_temp_minus = QPushButton('-', self)
        self.normal_temp_minus.clicked.connect(self.normal_temp_control_minus)
        self.normal_temp_minus.setGeometry(1400,400,100,100)

        self.alarm_temp_title = QLabel(self)
        self.alarm_temp_title.setText('設置報警溫度值 :             °C  ')
        self.alarm_temp_title.setGeometry(250,550,1230,100) # (水平, 垂直, 寬度, 高度)

        self.alarm_temp_add = QPushButton('+', self)
        self.alarm_temp_add.clicked.connect(self.alarm_temp_control_add)
        self.alarm_temp_add.setGeometry(1550,550,100,100) 

        self.alarm_temp_edit = QLineEdit(self)
        self.alarm_temp_edit.setText(str(self.alarm_temp_setting))
        self.alarm_temp_edit.setGeometry(950,550,200,100) 

        self.alarm_temp_minus = QPushButton('-', self)
        self.alarm_temp_minus.clicked.connect(self.alarm_temp_control_minus)
        self.alarm_temp_minus.setGeometry(1400,550,100,100) 

        self.btn_finish = QPushButton('確定', self)
        self.btn_finish.clicked.connect(self.close)
        self.btn_finish.setGeometry(870,750,200,100) 

        self.normal_temp_title.setFont(QFont("Roman times",60,QFont.Bold))
        self.normal_temp_edit.setFont(QFont("Roman times",60,QFont.Bold))
        self.normal_temp_add.setFont(QFont("Roman times",60,QFont.Bold))
        self.normal_temp_minus.setFont(QFont("Roman times",60,QFont.Bold))
        self.alarm_temp_title.setFont(QFont("Roman times",60,QFont.Bold))
        self.alarm_temp_edit.setFont(QFont("Roman times",60,QFont.Bold))
        self.alarm_temp_add.setFont(QFont("Roman times",60,QFont.Bold))
        self.alarm_temp_minus.setFont(QFont("Roman times",60,QFont.Bold))
        self.btn_finish.setFont(QFont("Roman times",60,QFont.Bold))

        self.setGeometry(300,250,1400,600) # 視窗顯示位置
        self.setWindowTitle("溫度設定")

    def normal_temp_control_add(self):
        self.normal_temp_setting += 0.1
        self.normal_temp_edit.setText(str(round(self.normal_temp_setting, 1)))
        
        self.temp_dict['normal_temp_setting'] = round(self.normal_temp_setting, 1)

        with open(self.filepath, "w+") as output:
            output.write(str(self.temp_dict))

    def normal_temp_control_minus(self):
        self.normal_temp_setting -= 0.1
        self.normal_temp_edit.setText(str(round(self.normal_temp_setting, 1)))

        self.temp_dict['normal_temp_setting'] = round(self.normal_temp_setting, 1)
        
        with open(self.filepath, "w+") as output:
            output.write(str(self.temp_dict))

    def alarm_temp_control_add(self):
        self.alarm_temp_setting += 0.1
        self.alarm_temp_edit.setText(str(round(self.alarm_temp_setting, 1)))

        self.temp_dict['alarm_temp_setting'] = round(self.alarm_temp_setting, 1)

        with open(self.filepath, "w+") as output:
            output.write(str(self.temp_dict))

    def alarm_temp_control_minus(self):
        self.alarm_temp_setting -= 0.1
        self.alarm_temp_edit.setText(str(round(self.alarm_temp_setting, 1)))

        self.temp_dict['alarm_temp_setting'] = round(self.alarm_temp_setting, 1)

        with open(self.filepath, "w+") as output:
            output.write(str(self.temp_dict))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    #ex.showFullScreen()
    sys.exit(app.exec_()) 

