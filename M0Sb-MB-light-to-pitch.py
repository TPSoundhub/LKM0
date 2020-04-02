# M0Sb-MB-light-to-pitch.py
#-----------------------------
# Revision 0.3 - 02 apr 2020 - Knud Funch, Soundhub Danmark - LYDKit til undervisningsbrug - Region MidtJylland
# 
# - An exampel where light intensity are converted to a frequency played back on speaker connected to pin 0 and GND
#
# Can you hear the light intensity? Try it out! Connect a speaker +/- to GND and PIN 0 on MB.
# Can use wired headphones. On minijack: tip = left, next ring is right, and next is GND.  
#
# Do not get pitch at or above 3900 then it crash! and below 30 not a lot to hear
# light value returned when reading light level is 0-255
#
# Can you change the program to use magnetometer input instead of light to generate sound?
#
# See the official MicroPython documentation on: https://microbit-micropython.readthedocs.io/en/latest/
# 
from microbit import *
import music

old_light_high = 0
old_light_low = 255

while True:
    light=display.read_light_level()
    freq = light*14+0
    music.pitch(freq, 6)
