# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:47:38 2021

@author: kullanici
"""

from Ax12 import Ax12

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = 'COM4'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 1
motor_id1 = 1
my_dxl = Ax12(motor_id1)  
my_dxl.set_moving_speed(200)
my_dxl.set_goal_position(512)

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


def user_input():
    """Check to see if user wants to continue"""
    ans = input('do you want to update the angle? : y/n ')
    if ans == 'n':
        return False
    else:
        return True
    
def user_input2():
    """Check to see if user wants to continue"""
    ans = input('Do you want to choose another motor? : y/n ')
    if ans == 'n':
        return False
    else:
        return True


def main(motor_object):
    """ sets goal position based on user input """
   
    bool_test = True
    while bool_test:

        print("\nPosition of dxl ID: %d is %d " %
              (motor_object.id, motor_object.get_present_position()))
        # desired angle input
        input_pos = (int(input("goal pos: ")))*1024/300
        motor_object.set_goal_position(input_pos)
        print("Position of dxl ID: %d is now: %d " %
              (motor_object.id, motor_object.get_present_position()))
        bool_test = user_input()

# pass in AX12 object
bool_test = True
while bool_test:
    
    motor_num = int(input("Select motor number: 1-2-3-4\n"))
    if motor_num == 1:
        main(my_dxl)
    elif motor_num == 2:
        main(my_dx2)
    elif motor_num == 3:
        main(my_dx3)
    elif motor_num == 4:
        main(my_dx4)
    else:
        print("wrong choice")
    bool_test = user_input2()

# disconnect

my_dxl.set_torque_enable(0)

my_dx2.set_torque_enable(0)
 
my_dx3.set_torque_enable(0)
 
my_dx4.set_torque_enable(0)
Ax12.disconnect()
