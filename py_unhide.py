import argparse
from PIL import Image

# get next 3 pixels which is the next character
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

    return(pixel_1_width,pixel_1_height,pixel_2_width,pixel_2_height,pixel_3_width,pixel_3_height)

## extracts bits of message from a pixel
def extractbit(pixel):
    pixcol = 0
    bits = ""
    pixel = list(pixel)
    while pixcol <= 2:
        remainder = int(pixel[pixcol]) % 2
        if remainder == 0:
            bits = bits + "0"
        else:
            bits = bits + "1"
        pixcol = pixcol+1
    return bits

## CLI switches
parser = argparse.ArgumentParser(prog='py_unhide.py', description='extracts messages from bmp file hidden by py_hide.py')
parser.add_argument('--input', required=True, help='Input picture file')

args = parser.parse_args()

input_file = args.input

input_image = Image.open(input_file)

with input_image as im:
    # load pixels in to px
    px = im.load()

# set image size variables
img_height = im.size[1]
img_width = im.size[0]

# prepring variables
current_h = 0
current_w = 0
foundfullmessage = 0
message = ""

# extract message from picture
while foundfullmessage == 0:
    p1_w, p1_h, p2_w, p2_h, p3_w, p3_h = get_next_3_pixels(current_w, current_h, img_width)

    p1_char_bits = extractbit(px[p1_w, p1_h])
    p2_char_bits = extractbit(px[p2_w, p2_h])
    p3_char_bits = extractbit(px[p3_w, p3_h])

    # checking if this is the last character in the message
    if p3_char_bits[2:] == "0":
        foundfullmessage = 1

    character = p1_char_bits+p2_char_bits+p3_char_bits[:2]

    # Initializing a binary string in the form of
    # 0 and 1, with base of 2
    binary_int = int(character, 2)
    # Getting the byte number
    byte_number = binary_int.bit_length() + 7 // 8
    # Getting an array of bytes
    binary_array = binary_int.to_bytes(byte_number, "big")
    # Converting the array into ASCII text
    ascii_character = binary_array.decode()
    message = message + ascii_character
    print(message)

    # on to the next pixel and character
    current_w = current_w + 3
