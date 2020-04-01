# Can you hear the light intensity?
#
# Do not get pitch at or above 3900 then it crash! and below 30 not mush to hear
# light value returned when reading light levet is 0-255
#
from microbit import *
import music

old_light_high = 0
old_light_low = 255

while True:
    light=display.read_light_level()
    freq = light*14+0
    music.pitch(freq, 6)
