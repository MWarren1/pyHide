import argparse
from PIL import Image

def get_next_3_pixels(current_width, current_height, image_width):
    # making sure we dont over run the width
    if current_width + 2 >= image_width:
        current_height = current_height + 1
        current_width = 0
    # pixel 1
    pixel_1_width = current_width
    pixel_1_height = current_height
    # pixel 2
    pixel_2_width = current_width + 1
    pixel_2_height = current_height
    # pixel 3
    pixel_3_width = current_width + 2
    pixel_3_height = current_height

    return(pixel_1_width,  \
           pixel_1_height, \
           pixel_2_width,  \
           pixel_2_height, \
           pixel_3_width,  \
           pixel_3_height)

## function to check if pixel colour values are 255(max)
def pixelcolourcheck(pixel):
    pixcol = 0
    pixel = list(pixel)
    while pixcol <= 2:
        # if pixel is max colour value then reduce it
        if pixel[pixcol] == 255:
            pixel[pixcol] = 254
        pixcol = pixcol+1
    pixel = tuple(pixel)
    return pixel

## puts part of character in a single pixel
def encryptpixel(pixel,charpart):
    pixcol = 0
    pixel = list(pixel)

    while pixcol <= 2:
        # devide colour value by 2
        remainder = int(pixel[pixcol]) % 2

        if charpart[pixcol] == "1":
            # if remainder is 0 colour value is even and needs to be made odd
            if remainder == 0:
                pixel[pixcol] = pixel[pixcol] + 1
        else:
            # if remainder is 1 colour value is odd and needs to be made even
            if remainder != 0:
                pixel[pixcol] = pixel[pixcol] + 1
        pixcol = pixcol+1

    # convert pixel back to tuple
    pixel = tuple(pixel)
    return pixel

def encryptletter(pixel1,pixel2,pixel3,char,last):
    # spilt up the letter in to 3 bits one for each pixel
    charpart1 = char[0:3]
    charpart2 = char[3:6]
    charpart3 = char[6:] + last

    # check each pixel to see if it is ma colour value
    pixel1 = pixelcolourcheck(pixel1)
    pixel2 = pixelcolourcheck(pixel2)
    pixel3 = pixelcolourcheck(pixel3)

    # add letter binary to colour values of pixels
    pixel_1_after = encryptpixel(pixel1,charpart1)
    pixel_2_after = encryptpixel(pixel2,charpart2)
    pixel_3_after = encryptpixel(pixel3,charpart3)
    return[pixel_1_after, pixel_2_after, pixel_3_after]

## CLI switches
parser = argparse.ArgumentParser(prog="py_hide.py", \
                                 description="Hides message in a bmp image")

parser.add_argument("--input", required=True, \
                    help="Input bmp image file")

parser.add_argument("--message", required=True, \
                    help="Message to hide in the bmp image")

args = parser.parse_args()

input_file = args.input
message = args.message

## convert message to a binary list
binary_message_list = []
for letter in message:
    binary_message_list.append(format(ord(letter), "08b"))

message_length = len(message)

print(binary_message_list)

input_image = Image.open(input_file)
output_image = input_image.copy()

# open input image
with output_image as im:
    # load pixels in to px
    px = im.load()
print("Image size: " + str(im.size))
img_height = im.size[1]
img_width = im.size[0]

# preping variables
current_h = 0
current_w = 0
current_letter = 0
output_file = "output-" + input_file


for letter in binary_message_list:
    #find out if this is the last letter in the message
    if current_letter + 1 == message_length:
        last_bit = "0"
    else:
        last_bit = "1"

    p1_w, p1_h, p2_w, p2_h, p3_w, p3_h = get_next_3_pixels(current_w, \
                                                           current_h, \
                                                           img_width)

    # getting pixel data
    p1_values = px[p1_w, p1_h]
    p2_values = px[p2_w, p2_h]
    p3_values = px[p3_w, p3_h]

    # get new pixel values
    p1_values_after,p2_values_after,p3_values_after = encryptletter(p1_values, \
                                                                    p1_values, \
                                                                    p1_values, \
                                                                    letter,    \
                                                                    last_bit)

    # update pixel values
    output_image.putpixel((p1_w, p1_h), p1_values_after)
    output_image.putpixel((p2_w, p2_h), p2_values_after)
    output_image.putpixel((p3_w, p3_h), p3_values_after)

    print(letter)
    print("p1 before : "+str(p1_values)+" after : "+str(p1_values_after))
    print("p2 before : "+str(p2_values)+" after : "+str(p2_values_after))
    print("p3 before : "+str(p3_values)+" after : "+str(p3_values_after))
    print("--------------------------------")

    # moving on to next letter
    current_letter = current_letter + 1
    # getting next unused pixel for next leter
    current_w = current_w + 3

output_image.save(output_file, format="BMP")
