# Basic keyboard for LYDKit project P1 spring 2020. SSG, SHD, Herningsholm, Skanderborg - sponsered by Region MidtJylland
#
# Version 17 jan  2020, Knud Funch SHD
#
# Keybord - read pin 0-2 and combine into 7 key active/inactive that are sent on the seriel port so it eg can be used as
# 7 keys together with Tonegenertor for a demo
#
#
from microbit import *
import radio

# 10 char id "0123456789"
name =       "Sender A  "       # Write a unique name 

local_connected = True          # set this to FALSE for sending on radio instead of USB

def display_current_mode(lc):
    if lc:
        display.show(Image.SQUARE_SMALL)
    else:
        display.show(Image.SQUARE)

def send_streng(k):
    if local_connected:
        print(k+name)
    else:
        radio.send(k+name)

print("Hello World - Klar på den serielle ",name)

display_current_mode(local_connected)
sleep(2000)
display.clear()

radio.on()

while True:                  # Forever - at least until power off/reset - generate events on USB or radio
 
    sleep(50)                
    if button_a.was_pressed(): send_streng("A ")    
    if button_a.was_pressed(): send_streng("A ")
    
    if local_connected:
        r = radio.receive()
        if r: print(r)                      # send anything reeceived on USB if local connected


    
        

 

   
        
     
        
