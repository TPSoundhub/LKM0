# Basic event maker for LYDKit project P1 winter 2019. SSG, SHD, Herningsholm, Skanderborg - sponsered by Region MidtJylland
# Version 15 oktober 2019, Knud Funch SHD
# - Test of sensors - temp, magnetometer, light ..
#
# 
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
#     print("")
     print("Magnetic field: ",field, "xyz", mx,my,mz)
#     print("Ligth: ",light," Temp: ",temp, " Acc xyz: ", x,y,z)
     sleep(30)
             
            
           
                
             
                

