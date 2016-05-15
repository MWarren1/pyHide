############################# 
##        pyHide           ## 
##      Python 2.7         ## 
##   By Redemption.Man     ## 
############################# 

import Image
import random
import ImageDraw
import argparse

## CLI switches
parser = argparse.ArgumentParser(prog='pyHide.py', description='pyHide - hides messages in a png file')
parser.add_argument('--input', required=True, help='Input picture file')
parser.add_argument('--message', required=False, help='message to hide must have "" (eg "hello world")')
args = parser.parse_args()

inputfile = args.input
message = args.message
## convert message to a binary list
binarymessage = map(bin,bytearray(message))
totalletters = len(binarymessage)
currentletter = 0
while currentletter <= (totalletters-1):
	current = binarymessage[currentletter]
	start = current[0]
	end = current[2:]
	binarymessage[currentletter] = start + end
	currentletter = currentletter + 1
print binarymessage

## Loads input picture
im = Image.open(inputfile)
img = im.load()
## gets picture size
picsize = im.size
wsize = picsize[0]
hsize = picsize[1]
## checks if message is too long for picture and prints a warning if it is
totalpixels = wsize * hsize
maxw  = wsize/3
maxchar = maxw*hsize

if totalletters >= maxchar:
	print "***WARNING*** - message is too long for the input picture"

##### defining fuctions #####

## function to check if pixel colour values are 255(max)
def pixelcolourcheck(pixel):
	pixcol = 0
	pixel = list(pixel)
	while pixcol <= 2:
		if pixel[pixcol] == 255:
			pixel[pixcol] = 254;
		pixcol = pixcol+1
	pixel = tuple(pixel)
	return pixel;
	
## puts part of character in a single pixel
def encryptpixel(pixel,charpart):
	pixcol = 0
	pixel = list(pixel)
	pixel = list(pixel)
	while pixcol <= 2:
		remainder = int(pixel[pixcol]) % 2
		if charpart[pixcol] == "1":
			if remainder == 0:
				pixel[pixcol] = pixel[pixcol] + 1
		else:
			if remainder != 0:
				pixel[pixcol] = pixel[pixcol] + 1
		pixcol = pixcol+1
	pixel = tuple(pixel)
	return pixel;
	
def encryptletter(pixel1,pixel2,pixel3,char,last):
	charpart1 = char[0:3]
	charpart2 = char[3:6]
	charpart3 = char[6:] + last
	pixel1 = pixelcolourcheck(pixel1);
	pixel2 = pixelcolourcheck(pixel2);
	pixel3 = pixelcolourcheck(pixel3);

	return1 = encryptpixel(pixel1,charpart1);
	return2 = encryptpixel(pixel2,charpart2);
	return3 = encryptpixel(pixel3,charpart3);
	return[return1,return2,return3];
	
	


## create output image same size
outputim = Image.new( 'RGB', (wsize,hsize))
outputimg = outputim.load() # create the pixel map
draw = ImageDraw.Draw(outputim)

currentw = 0
currenth = 0
currentletter = 0
print totalletters
while currentletter <= (totalletters-1):
	char = binarymessage[currentletter]
	if (currentw+3) >= (wsize-1):
		currenth = currenth + 1
		currentw = 0
	pixel1 = img[currentw,currenth]
	p1w = currentw
	p1h = currenth
	currentw = currentw + 1
	pixel2 = img[currentw,currenth]
	p2w = currentw
	p2h = currenth
	currentw = currentw + 1
	pixel3 = img[currentw,currenth]
	p3w = currentw
	p3h = currenth
	currentw = currentw + 1
	if currentletter == (totalletters-1):
		last = "0"
	else:
		last = "1"
	while len(char) <= 7:
		char = "0"+char
	print char+last
	finalpixels = encryptletter(pixel1,pixel2,pixel3,char,last);
	print "before : "+str(pixel1)+" after : "+str(finalpixels[0])
	print "before : "+str(pixel2)+" after : "+str(finalpixels[1])
	print "before : "+str(pixel3)+" after : "+str(finalpixels[2])
	print outputimg[p1w,p1h]
	
	outputimg[p1w,p1h] = finalpixels[0]
	outputimg[p2w,p2h] = finalpixels[1]
	outputimg[p3w,p3h] = finalpixels[2]
	print outputimg[p1w,p1h]
	
	currentletter = currentletter + 1
## finsh off line
while currentw <= (wsize-1):
	outputimg[currentw,currenth] = img[currentw,currenth]
	currentw = currentw+1
currenth = currenth + 1 
## finish off picture
while currenth <= (hsize-1):
	currentw = 0
	while currentw <= (wsize-1):
		outputimg[currentw,currenth] = img[currentw,currenth]
		currentw = currentw+1
	currenth = currenth+1
	

outputim.save('output.png') 