# py_hide/py_unhide

my first attempt at steganography, 2 scripts one to hide a message in a png file and one to extract the message.
pyHide hides messages in png files and pyUnhide extracts the message from the png file

###### py_hide
```
usage: py_hide.py [-h] --input INPUT --message MESSAGE

hides message in a bmp image

options:
  -h, --help         show this help message and exit
  --input INPUT      Input bmp image file
  --message MESSAGE  Message to hide in the bmp image
```  
###### py_unhide
``` 
usage: py_unhide.py [-h] --input INPUT

extracts messages from png file hidden by py_hide.py

optional arguments:
  -h, --help     show this help message and exit
  --input INPUT  Input picture file
 ``` 
