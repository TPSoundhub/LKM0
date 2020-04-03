# M0Sa2-MB-pintokey.py
#------------------------
# Revision 0.4 - 03 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - An exampel where Pin 0,1 and 2 are converted to 7 key events and printed to the shell
#
# See the official MicroPython documentation on: https://microbit-micropython.readthedocs.io/en/latest/
#
# Can you 'count to 7' combining the 3 PINs. Run program and shortcut from GND to the pins in order so
# you get the number 1,2,3,4,5,6,7 printed in order into the shell.
# Can you make a physical keyboard with conductive tape, cardboard and wires?
#
from microbit import *

key = "0"
last_key = "0"

display.clear()

while True:

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

    if last_key!=key:
        print(key)
        last_key=key
        
    sleep(30)