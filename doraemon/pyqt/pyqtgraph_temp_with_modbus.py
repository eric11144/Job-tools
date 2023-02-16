import sys
from pyModbusTCP.client import ModbusClient
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QFrame, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont


class window(QWidget):
    def __init__(self):
        super().__init__()

        # Sub Window
        self.sub_window = SubWindow()

        self.normal = 0
        self.alarm = 0

        # Temperature title box
        self.temp_title = QLabel(self)
        self.temp_title.setText("<font color=%s>%s</font>" %('#00CED1', "檢測溫度 : "))
        self.temp_title.setFrameShape(QFrame.Box)
        self.temp_title.setFrameShadow(QFrame.Raised)
        self.temp_title.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(255, 255, 255)')
        self.temp_title.setAlignment(Qt.AlignTop)
        self.temp_title.setGeometry(250,10,730,330) # (水平, 垂直, 寬度, 高度)

        # Temperature unit box
        self.unit = QLabel(self)
        self.unit.setText("<font color=%s>%s</font>" %('#00CED1', "°C"))
        self.unit.setGeometry(780,120,180,200) # (水平, 垂直, 寬度, 高度)

        # Temperature
        self.temp = QLabel(self)
        self.temp.setText("<font color=%s>%s</font>" %('#00CED1', "0.00"))
        self.temp.setGeometry(350,120,430,200) # (水平, 垂直, 寬度, 高度)

        # Title with number of people measured box
        self.title_with_number_of_people_measured = QLabel(self)
        self.title_with_number_of_people_measured.setText("<font color=%s>%s</font>" %('#00CED1', "測溫人數 : "))
        self.title_with_number_of_people_measured.setFrameShape(QFrame.Box)
        self.title_with_number_of_people_measured.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_people_measured.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(255, 255, 255)')
        self.title_with_number_of_people_measured.setAlignment(Qt.AlignTop)
        self.title_with_number_of_people_measured.setGeometry(10,10,220,160) 

        # Number of people measured box
        self.number_of_people_measured = QLabel(self)
        self.number_of_people_measured.setText("<font color=%s>%s</font>" %('#00CED1', "0"))
        self.number_of_people_measured.setGeometry(30,80,180,80) 

        # Title with number of alarm box
        self.title_with_number_of_alarm = QLabel(self)
        self.title_with_number_of_alarm.setText("<font color=%s>%s</font>" %('#00CED1', "報警次數 : "))
        self.title_with_number_of_alarm.setFrameShape(QFrame.Box)
        self.title_with_number_of_alarm.setFrameShadow(QFrame.Raised)
        self.title_with_number_of_alarm.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(255, 255, 255)')
        self.title_with_number_of_alarm.setAlignment(Qt.AlignTop)
        self.title_with_number_of_alarm.setGeometry(10,180,220,160)

        # Number of alarm
        self.number_of_alarm = QLabel(self)
        self.number_of_alarm.setText("<font color=%s>%s</font>" %('#00CED1', "0"))
        self.number_of_alarm.setGeometry(30,260,180,70) 

        # Setting normal & alarm temp bottom
        self.btn_setting_with_temp_upper_and_lower_limits = QPushButton('設定', self)
        self.btn_setting_with_temp_upper_and_lower_limits.setStyleSheet("color: darkturquoise")
        self.btn_setting_with_temp_upper_and_lower_limits.clicked.connect(self.sub_window.show) 
        self.btn_setting_with_temp_upper_and_lower_limits.setGeometry(990,10,200,100)

        # Scan box
        self.scan = QLabel(self)
        self.scan.setText("<font color=%s>%s</font>" %('#00CED1', "量測中....."))
        self.scan.setFrameShape(QFrame.Box)
        self.scan.setFrameShadow(QFrame.Raised)
        self.scan.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(255, 255, 255)')
        self.scan.setAlignment(Qt.AlignCenter)
        self.scan.setGeometry(990,120,200,220)

        # Start bottom
        self.btn_start = QPushButton('開始', self)
        self.btn_start.setStyleSheet("color: darkturquoise")
        self.btn_start.clicked.connect(self.start) 
        self.btn_start.setGeometry(10,360,110,130)        

        # Clean bottom
        self.btn_clean = QPushButton('清零', self)
        self.btn_clean.setStyleSheet("color: darkturquoise")
        self.btn_clean.clicked.connect(self.clean) 
        self.btn_clean.setGeometry(130,360,110,130)

        # Announcement box
        self.announcement = QLabel(self)
        self.announcement.setText("<font color=%s>%s</font>" %('#00CED1', "請保持 1 米距離, 戴口罩, 勤洗手!!"))
        self.announcement.setFrameShape(QFrame.Box)
        self.announcement.setFrameShadow(QFrame.Raised)
        self.announcement.setStyleSheet('border-width: 2px; border-style: solid; border-color:rgb(255, 255, 255)')
        self.announcement.setAlignment(Qt.AlignCenter)
        self.announcement.setGeometry(250,360,940,130) 

        # 設訂字體及大小
        self.temp_title.setFont(QFont("Roman times",30,QFont.Bold))
        self.temp.setFont(QFont("Roman times",100,QFont.Bold))
        self.unit.setFont(QFont("Roman times",100,QFont.Bold))
        self.title_with_number_of_people_measured.setFont(QFont("Roman times",30,QFont.Bold))
        self.number_of_people_measured.setFont(QFont("Roman times",30,QFont.Bold))
        self.title_with_number_of_alarm.setFont(QFont("Roman times",30,QFont.Bold))
        self.number_of_alarm.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_start.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_clean.setFont(QFont("Roman times",30,QFont.Bold))
        self.btn_setting_with_temp_upper_and_lower_limits.setFont(QFont("Roman times",30,QFont.Bold))
        self.announcement.setFont(QFont("Roman times",30,QFont.Bold))
        self.scan.setFont(QFont("Roman times",30,QFont.Bold))

        # Windows show address
        self.setGeometry(500,200,1200,500) # 視窗顯示位置
        self.setStyleSheet('background-color: white')
        
        # Windows title name
        self.setWindowTitle("溫度監測")

    def start(self):
        self.modbus_open()

    def clean(self):
        self.init_count = 0
        self.number_of_people_measured.setText(str(self.init_count))
        self.number_of_alarm.setText(str(self.init_count))

    def modbus_open(self):
        HOST = '192.168.11.130'
        PORT = 502

        c1 = ModbusClient()
        c1.host(HOST)
        c1.port(PORT)
        c1.unit_id(1)
        data = 0

        if not c1.is_open():
            if not c1.open():
                print("unable to connect to "+HOST+":"+str(PORT))

        if c1.is_open():
            # read 2 registers at address 0, store result in regs list
            regs = c1.read_holding_registers(30, 5)
            data = regs[0]

            self.temp.setText(str(data))
            
            normal_temp_text = self.sub_window.normal_temp_edit.text()
            normal_temp = float(normal_temp_text)

            alarm_temp_text = self.sub_window.alarm_temp_edit.text()
            alarm_temp = float(alarm_temp_text)

            if (normal_temp == 0.0 and alarm_temp == 0.0):
                self.scan.setText('量測中.....')
            elif normal_temp-5 <= data and data <= alarm_temp:
                self.scan.setText('溫度正常 \n, 請通過 \n')
            elif data >= normal_temp and data <= alarm_temp:
                self.scan.setText('溫度正常 \n, 請通過 \n')
            else:
                self.scan.setText('溫度異常 \n, 請留步 \n')
                self.alarm += 1
                self.number_of_alarm.setText(str(self.alarm))
            self.normal += 1
            self.number_of_people_measured.setText(str(self.normal))


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