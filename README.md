# py_hide/py_unhide

my first attempt at steganography, 2 scripts one to hide a message in a png file and one to extract the message.
pyHide hides messages in png files and pyUnhide extracts the message from the png file


### How it Works
1. each pixel has 3 colours (RGB) and each colour has a value from 0 to 255.
2. each colour can store 1 bit of data, where if the value is even that’s a 0 and if the value is odd it is a 1
3. each character of the message is converted into binary (1byte/8 bits)
4. if we take 3 consecutive pixels we can store 9 bits of binary, 8 bits (1 byte) for the character and the final bit is used to say if there is another character. This last bit is 1 if there is another character and 0 that is the final character of the message.

#### Example
1. message to hide is: apple
2. the first letter a is converted to binary: 01100001
3. as there is another letter after we will need to add a 1 to the binary: 011000011
4. we need to get the next 3 pixels and their colour values (Red, Green, Blue)
  - pixel 1 - (123, 111, 100)
  - pixel 2 - (123, 111, 100)
  - pixel 3 - (123, 111, 100)
5. split up the binary into 3 parts of 3 bits each. 011000011
  - 011
  - 000
  - 011
6. hide binary into the pixels, where if the value is 0 then the colour value needs to be even, and if the value is 1 then the colour value needs to be odd
  - Pixel 1 - Binary 011
    - Colour Value Before - (123, 111, 100)
    - Colour Value After - (124, 111, 101) - Even, Odd, Odd
  - Pixel 2 - Binary 000
    - Colour Value Before - (123, 111, 100)
    - Colour Value After - (124, 112, 100) - Even, Even, Even
  - Pixel 3 - Binary 011
    - Colour Value Before - (123, 111, 100)
    - Colour Value After - (124, 111, 101) - Even, Odd, Odd
7. This small colour value change is not visible to anyone who views the image, even if you know there is a message hidden.

### Notes/Limitations
- the get_next_3_pixels function could be improved on how it deals with the end of the width
- characters in message limited to (image_width-2)*image_height
- only does bmp image files, would prefer to use png image files

### Example of a image with hidden message

![alt text](example.bmp "Example with a hidden message")

### py_hide
```
usage: py_hide.py [-h] --input INPUT --message MESSAGE

hides message in a bmp image

options:
  -h, --help         show this help message and exit
  --input INPUT      Input bmp image file
  --message MESSAGE  Message to hide in the bmp image
```  
### py_unhide
``` 
usage: py_unhide.py [-h] --input INPUT

extracts messages from png file hidden by py_hide.py

optional arguments:
  -h, --help     show this help message and exit
  --input INPUT  Input picture file
 ``` 
