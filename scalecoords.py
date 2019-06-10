#!/usr/bin/env python

import math

def scaleLine(magnitude, angle, screenheight, screenwidth, originalHeight, originalWidth):
    h_ratio = float(screenheight)/originalHeight
    w_ratio = float(screenwidth)/originalWidth

    rangle = math.radians(angle % 90.0)
    quad = int(angle / 90.0)
    
    if angle == 0.0 or angle == 360.0 or angle == 180.0:
        return w_ratio * magnitude
    if angle == 90.0 or angle == 270.0:
        return h_ratio * magnitude

    t_height = (math.sin(rangle) if quad % 2 == 0 else math.cos(rangle)) * magnitude
    t_width = (math.cos(rangle) if quad % 2 == 0 else math.sin(rangle)) * magnitude
    return math.sqrt((t_height * h_ratio)**2.0 + (t_width * w_ratio)**2.0)

if __name__ == "__main__":
	originalHeight = 1280.0
	originalWidth = 768.0

	newHeight = 1920.0
	newWidth = 1080.0

	testAngle = 33.0
	testHeight = 80.0

	v1 = scaleLine(testHeight, testAngle, newHeight, newWidth, originalHeight, originalWidth)
  	print v1
  	print scaleLine(v1, testAngle, originalHeight, originalWidth, newHeight, newWidth)

	v1 = scaleLine(testHeight, testAngle, originalHeight, originalWidth, originalHeight, originalWidth)
  	print v1
  	print scaleLine(v1, testAngle, originalHeight, originalWidth, originalHeight, originalWidth)


