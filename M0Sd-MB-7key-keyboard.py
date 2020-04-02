# M0Sd-MB-pins-to-7key-events.py
#-------------------------------
# Revision 0.3 - 02 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - Program that convert PIN input to 0-7 keys and send on USB or on radio
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
name =       "MB 7Key 1 "

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
    p0 = pin0.is_touched()
    p1 = pin1.is_touched()
    p2 = pin2.is_touched()
    if p0 and p1 and p2:             key="7"
    if not p0 and p1 and p2:         key="6" 
    if p0 and not p1 and p2:         key="5" 
    if not p0 and not p1 and p2:     key="4"
    if p0 and p1 and not p2:         key="3"
    if not p0 and p1 and not p2:     key="2" 
    if p0 and not p1 and not p2:     key="1" 
    if not p0 and not p1 and not p2: key="0"   # no pins touched -> no key pressed  
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