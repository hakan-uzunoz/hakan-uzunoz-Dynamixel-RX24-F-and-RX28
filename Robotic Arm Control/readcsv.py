import csv
from Ax12 import Ax12
import time

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
margin= my_dx1.get_cw_compliance_margin()
speed= my_dx1.get_moving_speed()
print("slope: {} margin: {} speed: {}".format(slope,margin,speed))


"""
my_dx1.set_cw_compliance_slope(slope)
my_dx1.set_ccw_compliance_slope(slope)
my_dx2.set_cw_compliance_slope(slope)
my_dx2.set_ccw_compliance_slope(slope)
my_dx3.set_cw_compliance_slope(slope)
my_dx3.set_ccw_compliance_slope(slope)
my_dx4.set_cw_compliance_slope(slope)
my_dx4.set_ccw_compliance_slope(slope)

my_dx1.set_moving_speed(speed)
my_dx2.set_moving_speed(speed)
my_dx3.set_moving_speed(speed)
my_dx4.set_moving_speed(speed)

my_dx1.set_cw_compliance_margin(margin)
my_dx1.set_ccw_compliance_margin(margin)
my_dx2.set_cw_compliance_margin(margin)
my_dx2.set_ccw_compliance_margin(margin)
my_dx3.set_cw_compliance_margin(margin)
my_dx3.set_ccw_compliance_margin(margin)
my_dx4.set_cw_compliance_margin(margin)
my_dx4.set_ccw_compliance_margin(margin)
"""



def cal(num):
    value = int((float(num)+150)*1024/300)
    
    return value

with open('motor_aci(2).txt','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for n in range(5):
        for row in csv_reader:
            my_dx1.set_goal_position(cal(row[0]))
            my_dx2.set_goal_position(cal(row[1]))
            my_dx3.set_goal_position(cal(row[2]))
            my_dx4.set_goal_position(cal(row[3]))
            time.sleep(1)
            #print(cal(row[0]),cal(row[1]),cal(row[2]),cal(row[3]))
            
my_dx1.set_torque_enable(0)

my_dx2.set_torque_enable(0)
 
my_dx3.set_torque_enable(0)
 
my_dx4.set_torque_enable(0)
Ax12.disconnect()

            
        
    