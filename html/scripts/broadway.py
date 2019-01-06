import board
import neopixel
import random
import time

ORDER = neopixel.GRB

num_pixels = 30

pixels = neopixel.NeoPixel(board.D21, num_pixels, brightness=0.2, auto_write=False,pixel_order = ORDER)

pixel = 0
isEven = True

GOLD = (255,120,0)

pixels.fill((0,0,0))
pixels.show()

while(True):
	for i in range(0,num_pixels):
		if(isEven):
			if(i % 2 == 0):
				pixels[i] = GOLD
				pixels.show()
			else:
				pixels[i] = (0,0,0)
		else:
			if(i%2 == 0):
				pixels[i] = (0,0,0)
			else:
				pixels[i] = GOLD
	if(isEven):
		isEven = False
	else:
		isEven = True

	pixels.show()
	time.sleep(0.25)

