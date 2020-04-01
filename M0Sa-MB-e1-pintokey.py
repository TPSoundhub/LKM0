from microbit import *

key = "0"
last_key = "0"

display.clear()

while True:

    light=display.read_light_level()
    if   light>220:  key="7"
    elif light>170:  key="6" 
    elif light>125:  key="5" 
    elif light>100:  key="4"
    elif light> 90:  key="3"
    elif light> 80:  key="2" 
    elif light> 70:  key="1" 
    else:            key="0"  

    if last_key!=key:
        print(key)
        last_key=key
        
    sleep(50)