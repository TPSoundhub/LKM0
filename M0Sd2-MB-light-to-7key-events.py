# M0Sd2-MB-light-to-7key-events.py
#--------------------------------
# Revision 0.4 - 03 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - Program that convert light intensity to 0-7 keys and send on USB or on radio
# - Can switch between sending on USB or Radio with long press on both A and B keys.
# - Pressing both A and B at same time short displays current mode. That is:
#   - Small square for sending local - sending local activated keys and anything received on radio onto USB
#   - Large square for sending local activated keys onto radio to anyone listening.
#  - It always starts in local mode - so you have to switch mode before it start sending on radio (long press A and B)
#  - It displays 1-7 on local display when key is detected.
#
# See the official MicroPython documentation on: https://microbit-micropython.readthedocs.io/en/latest/
#
from microbit import *
import radio

# 10 char id "0123456789"
name =       "MBLightk 1"

last_key_sent = "0"
key_read_1    = "0"
key_read_2    = "0"

local_connected = True

def display_current_mode(lc):
    if lc: display.show(Image.SQUARE_SMALL)
    else: display.show(Image.SQUARE)

def check_mode_shift():
    global local_connected
    both_pressed = button_a.is_pressed() and button_b.is_pressed()
    if both_pressed:
        display_current_mode(local_connected)
        sleep(3000)
        display.clear()
        both_pressed = button_a.is_pressed() and button_b.is_pressed()
        if both_pressed:  # still after 3 sec
            if local_connected: local_connected = False
            else: local_connected = True
            display_current_mode(local_connected)
            sleep(3000)
            display.clear()

def read_key():
    light=display.read_light_level()
    if   light>220:  key="7"
    elif light>170:  key="6" 
    elif light>125:  key="5" 
    elif light>100:  key="4"
    elif light> 90:  key="3"
    elif light> 80:  key="2" 
    elif light> 70:  key="1" 
    else:            key="0"   # low light -> no key   
    return(key)

def send_streng(k):
    if local_connected: print(k+name)
    else: radio.send(k+name)

print("Hello World - Klar på den serielle ",name)

display.show(Image.HAPPY)
sleep(2000)
display.clear()

radio.on()

while True:                  # Forever - at least until power off/reset - generate events on USB or radio
    
    key_read_1 = read_key()
    sleep(50)                # 2 readings with same to detect for removing worst jitter
    key_read_2 = read_key()

    if (key_read_1 == key_read_2) and (key_read_1 != last_key_sent):
        send_streng(key_read_1)
        if key_read_1 == "0": display.clear()
        else:display.show(key_read_1) 
        last_key_sent = key_read_1
        
    check_mode_shift()
    
    if local_connected:
        r = radio.receive()
        if r: print(r)
#
# How could M0Sd..  M0Se.. and M0Sf... easily be combined? They do not differ that much do they?
#