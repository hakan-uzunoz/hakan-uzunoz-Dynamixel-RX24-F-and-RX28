from PyQt5 import QtWidgets
import sys
from dosyaadi import Ui_txt_sayi1
from Ax12 import Ax12

Ax12.DEVICENAME = 'COM4'
Ax12.BAUDRATE = 1_000_000
Ax12.connect()

motor_id1 = 1
my_dx1 = Ax12(motor_id1)  
my_dx1.set_moving_speed(200)
my_dx1.set_goal_position(512)

motor_id2 = 2
my_dx2 = Ax12(motor_id2)  
my_dx2.set_moving_speed(200)
my_dx2.set_goal_position(512)

motor_id3 = 3
my_dx3 = Ax12(motor_id3)  
my_dx3.set_moving_speed(200)
my_dx3.set_goal_position(512)

motor_id4 = 4
my_dx4 = Ax12(motor_id4)  
my_dx4.set_moving_speed(200)
my_dx4.set_goal_position(512)



slope = my_dx1.get_cw_compliance_slope()
margin = my_dx1.get_cw_compliance_margin()
speed = my_dx1.get_moving_speed()
torque = my_dx1.get_torque_limit()
id1 = str(my_dx1.get_model_number())
id2 = str(my_dx2.get_model_number())
id3 = str(my_dx3.get_model_number())
id4 = str(my_dx4.get_model_number())
temp1 = my_dx1.get_temperature()
temp2 = my_dx2.get_temperature()
temp3 = my_dx3.get_temperature()
temp4 = my_dx4.get_temperature()
volt1 = my_dx1.get_voltage()
volt2 = my_dx2.get_voltage()
volt3 = my_dx3.get_voltage()
volt4 = my_dx4.get_voltage()



class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_txt_sayi1()
        self.ui.setupUi(self)
        
        
        
        self.ui.verticalSlidr.valueChanged[int].connect(self.change)
        self.ui.verticalSlider_2.valueChanged[int].connect(self.change)
        self.ui.verticalSlider_3.valueChanged[int].connect(self.change)
        self.ui.verticalSlider_4.valueChanged[int].connect(self.change)
        self.ui.horizontalSlider.valueChanged[int].connect(self.change)
        self.ui.horizontalSlider_2.valueChanged[int].connect(self.change)
        self.ui.horizontalSlider_3.valueChanged[int].connect(self.change)
        self.ui.horizontalSlider_4.valueChanged[int].connect(self.change)
        
        self.ui.horizontalSlider.setProperty("value", slope)
        self.ui.horizontalSlider_2.setProperty("value", speed)
        self.ui.horizontalSlider_3.setProperty("value", margin)
        self.ui.horizontalSlider_4.setProperty("value", torque)
        
        self.ui.label_15.setText("Motor 1 Model: "+id1)
        self.ui.label_17.setText("Motor 2 Model: "+id2)
        self.ui.label_19.setText("Motor 3 Model: "+id3)
        self.ui.label_20.setText("Motor 4 Model: "+id4)
        self.ui.label_18.setText("Motor 1 Temp: "+str(temp1))
        self.ui.label_21.setText("Motor 2 Temp: "+str(temp2))
        self.ui.label_22.setText("Motor 3 Temp: "+str(temp3))
        self.ui.label_14.setText("Motor 4 Temp: "+str(temp4))
        self.ui.label_24.setText("Motor 1 Volt: "+str(volt1))
        self.ui.label_25.setText("Motor 2 Volt: "+str(volt2))
        self.ui.label_23.setText("Motor 3 Volt: "+str(volt3))
        self.ui.label_26.setText("Motor 4 Volt: "+str(volt4))
        self.ui.pushButton_3.clicked.connect(self.info)
        self.ui.pushButton.clicked.connect(self.tqd)
        self.ui.pushButton_2.clicked.connect(self.tqe)
        
    
    def change(self,value):
        sender = self.sender().objectName()
        if sender == "verticalSlidr":
            self.ui.label_7.setText(str(round(value/1023*300-150,2)))
            my_dx1.set_goal_position(int(value))
            error = my_dx1.get_alarm_led()
            if error == bin(2):
                self.ui.label_30.setText("Angel Limit: Error Occur")
            elif error == bin(8):
                self.ui.label_31.setText("Range: Error Occur")
            elif error == bin(16):
                self.ui.label_32.setText("Overload: Error Occur")
        elif sender == "verticalSlider_2":
            self.ui.label_8.setText(str(round(value/1023*300-150,2)))
            my_dx2.set_goal_position(int(value))
        elif sender == "verticalSlider_3":
            self.ui.label_9.setText(str(round(value/1023*300-150,2)))
            my_dx3.set_goal_position(int(value))
        elif sender == "verticalSlider_4":
            self.ui.label_10.setText(str(round(value/1023*300-150,2)))
            my_dx4.set_goal_position(int(value))
        elif sender == "horizontalSlider":
            self.ui.lcdNumber.display(str(value))
            my_dx1.set_cw_compliance_slope(2**value)
            my_dx1.set_ccw_compliance_slope(2**value)
            my_dx2.set_cw_compliance_slope(2**value)
            my_dx2.set_ccw_compliance_slope(2**value)
            my_dx3.set_cw_compliance_slope(2**value)
            my_dx3.set_ccw_compliance_slope(2**value)
            my_dx4.set_cw_compliance_slope(2**value)
            my_dx4.set_ccw_compliance_slope(2**value)
            
        elif sender == "horizontalSlider_2":
            self.ui.lcdNumber_2.display(str(round(value*0.111,1)))
            my_dx1.set_moving_speed(int(value))
            my_dx2.set_moving_speed(int(value))
            my_dx3.set_moving_speed(int(value))
            my_dx4.set_moving_speed(int(value))
        elif sender == "horizontalSlider_3":
            self.ui.lcdNumber_3.display(str(round(value,1)))
            my_dx1.set_cw_compliance_margin(int(value))
            my_dx1.set_ccw_compliance_margin(int(value))
            my_dx2.set_cw_compliance_margin(int(value))
            my_dx2.set_ccw_compliance_margin(int(value))
            my_dx3.set_cw_compliance_margin(int(value))
            my_dx3.set_ccw_compliance_margin(int(value))
            my_dx4.set_cw_compliance_margin(int(value))
            my_dx4.set_ccw_compliance_margin(int(value))
        elif sender == "horizontalSlider_4":
            self.ui.lcdNumber_4.display(str(round(value)))
            my_dx1.set_torque_limit(int(value))
            my_dx2.set_torque_limit(int(value))
            my_dx3.set_torque_limit(int(value))
            my_dx4.set_torque_limit(int(value))
            
            
    def info(self):
        
        self.ui.label_18.setText("Motor 1 Temp: "+str(temp1))
        self.ui.label_18.setText("Motor 1 Temp: "+str(temp1))
        self.ui.label_21.setText("Motor 2 Temp: "+str(temp2))
        self.ui.label_22.setText("Motor 3 Temp: "+str(temp3))
        self.ui.label_14.setText("Motor 4 Temp: "+str(temp4))
        self.ui.label_24.setText("Motor 1 Volt: "+str(volt1))
        self.ui.label_25.setText("Motor 2 Volt: "+str(volt2))
        self.ui.label_23.setText("Motor 3 Volt: "+str(volt3))
        self.ui.label_26.setText("Motor 4 Volt: "+str(volt4))
    
    def tqd(self):
        my_dx1.set_torque_enable(0)

        my_dx2.set_torque_enable(0)
 
        my_dx3.set_torque_enable(0)
 
        my_dx4.set_torque_enable(0)
    
    def tqe(self):
        my_dx1.set_torque_enable(1)

        my_dx2.set_torque_enable(1)
 
        my_dx3.set_torque_enable(1)
 
        my_dx4.set_torque_enable(1)    
        
        
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    
    win.show()
    sys.exit(app.exec_())

app()

my_dx1.set_torque_enable(0)

my_dx2.set_torque_enable(0)
 
my_dx3.set_torque_enable(0)
 
my_dx4.set_torque_enable(0)
Ax12.disconnect()






