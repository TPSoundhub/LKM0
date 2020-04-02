# M0Sc-MB-basic-radio.py
#------------------------
# Revision 0.3 - 02 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - An basic exampel of sending A/B key pres on the USB or alternative on radio to another one sending it on USB
#
# See the official MicroPython documentation on: https://microbit-micropython.readthedocs.io/en/latest/
#
# Go together two and two and make one to send on radio (change "local_connected" to True and "name" to a unique
# string. Run programs on both and see what comes through in the shell.
#
# Try to store the program sending on radio onto the MB sending on radio via "save as" in file menu. Store it
# with the name "main.py". Before doing so you must stop the program from within Thonny.
#
# Connect the MB to a battery pack as turn it on. Can you still send/receive..
#
from microbit import *
import radio

# 10 char id "0123456789"
name =       "Sender A  "       # Write a unique name - Do keep the lenght to 10 chars.

local_connected = False         # set this to FALSE for sending on radio instead of USB

def display_current_mode(lc):
    if lc: display.show(Image.SQUARE_SMALL)
    else:  display.show(Image.SQUARE)

def send_streng(k):
    if local_connected: print(k+name)
    else: radio.send(k+name)

print("Hello World - Klar på den serielle ",name)   # if connected on USB then send name no matter the mode.

# Show small square on MBs local display if it is in local send mode. Big square when in radio send mode.
display_current_mode(local_connected)  

radio.on()

# Forever - at least until power off/reset - generate events on USB or radio
while True:                 
# You can change the 3 lines below to anything you want to send     
    sleep(50)                
    if button_a.was_pressed(): send_streng("A fra: ")    
    if button_b.was_pressed(): send_streng("B fra: ")
    
# Keep the 3 lines below to pass anything received on radio on to the USB/seriel port
    if local_connected:
        r = radio.receive()
        if r: print(r)             


    
        

 

   
        
     
        
