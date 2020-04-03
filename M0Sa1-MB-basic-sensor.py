# M0Sa1-MB-basic-sensor.py
#------------------------
# Revision 0.4 - 03 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - Test of build-in sensors on standalone MB - Accelerometer, temp, magnetometer, light ..
# - If you want to focus on on sensor just remove some code and modify the rest .. Just try it out.
# - To make sure you can come back save a copy - but you can always get back as it is on GITHUB
#
# See the official MicroPython documentation on: https://microbit-micropython.readthedocs.io/en/latest/
#
from microbit import *

print("Hello World - Klar på den serielle")    # Ready
display.show(Image.HAPPY)
sleep(1000)
# Light sensor works even without using display.off()  
display.clear()

while True:                                                                                                          
    
     field=compass.get_field_strength()
     mx = compass.get_x()
     my = compass.get_y()
     mz = compass.get_z()
     light=display.read_light_level()
     temp=temperature()
     x,y,z=accelerometer.get_values()
     print("")
     print("Magnetic field: ",field, "xyz", mx,my,mz)
     print("Ligth: ",light," Temp: ",temp, " Acc xyz: ", x,y,z)
     sleep(100)  # in milliseconds
             
            
           
                
             
                

