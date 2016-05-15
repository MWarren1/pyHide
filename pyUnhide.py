############################# 
##       pyUnhide          ## 
##      Python 2.7         ## 
##   By Redemption.Man     ## 
############################# 


import Image
import random
import ImageDraw
import argparse

## CLI switches
parser = argparse.ArgumentParser(prog='pyUnhide.py', description='extracts messages from png file hidden by hide.py')
parser.add_argument('--input', required=True, help='Input picture file')

args = parser.parse_args()

#mode = args.mode
#if mode.lower() != "hide" || mode.lower() != "unhide"

inputfile = args.input

## Loads input picture
im = Image.open(inputfile)
img = im.load()
## gets picture size
picsize = im.size
wsize = picsize[0]
hsize = picsize[1]

##### defining fuctions #####
	
## extracts bits of message from a pixel
def extractbit(pixel):
	pixcol = 0
	pixel = list(pixel)
	while pixcol <= 2:
		remainder = int(pixel[pixcol]) % 2
		if remainder == 0:
			pixel[pixcol] = "0"
		else:
			pixel[pixcol] = "1"
		pixcol = pixcol+1
	bits = tuple(pixel)
	return bits;
	
	
## find pixels that conatin the message	
foundfullmessage = 0
currenth = 0
currentw = 0
msglist = []
count = 1
currentchar = ""
while foundfullmessage == 0:
		currentpixel = img[currentw,currenth]
		bits = extractbit(currentpixel)
		if count == 1 or count == 2:
			currentchar = currentchar + bits[0] + bits[1] + bits[2]
		else:
			count = 0
			currentchar = currentchar + bits[0] + bits[1]
			msglist.append(currentchar)
			currentchar = ""
			if bits[2] == "0":
				foundfullmessage = 1

		currentw = currentw+1
		count = count+1
print msglist
## convert binary to characters

charnum = len(msglist)
currentchar = 0
message = ""
while currentchar <= (charnum-1):
	char = chr(int(msglist[currentchar], 2))
	message = message + char
	print message
	currentchar = currentchar + 1

