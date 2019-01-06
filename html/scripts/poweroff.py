import board
import neopixel
import random
import time

ORDER = neopixel.GRB

num_pixels = 30

#define brightness
brightness_min = 0.1

#define how fast fade is between intervals of fading.
#for example, if min was 0.1 and max was 1.0, you have 9 brightness changes, to make it smooth.
#number of brightness changes * fade_time = time it takes to complete the change
#smaller the number, the faster the change.
fade_time = 0.1

#define object. brightness is inconsequential here, since we are manipulating it.
pixels = neopixel.NeoPixel(board.D21, num_pixels, brightness=1.0, auto_write=False,pixel_order = ORDER)

def fade(brightness):
	pixels.brightness = brightness
	pixels.show()

#insert fancy animation here?
pixels.fill((0,0,255))

#fade out
i = pixels.brightness
while(i > 0.1):
	fade(i)
	i = i - 0.1
	time.sleep(fade_time)

#power off
pixels.fill((0,0,0))
pixels.show()
