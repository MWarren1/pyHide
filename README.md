# py_hide/py_unhide

my first attempt at steganography, 2 scripts one to hide a message in a png file and one to extract the message.
pyHide hides messages in png files and pyUnhide extracts the message from the png file

### Notes/Limitations
- the get_next_3_pixels function could be improved on how it deals with the end of the width
- characters in message limited to (image_width-2)*image_height
- only does bmp image files, would prefer to use png image files

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
