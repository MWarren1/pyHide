# pyHide/pyUnhide
###### Dependencies : Python 2.7
###### By Redemption.Man

my first attempt at steganography, 2 scripts one to hide a message in a png file and one to extract the message.
pyHide hides messages in png files and pyUnhide extracts the message from the png file

###### pyHide
```
usage: pyHide.py [-h] --input INPUT [--message MESSAGE]

pyHide - hides messages in a png file

optional arguments:
  -h, --help         show this help message and exit
  --input INPUT      Input picture file
  --message MESSAGE  message to hide must have "" (eg "hello world")
```  
###### pyUnhide
``` 
usage: pyUnhide.py [-h] --input INPUT

extracts messages from png file hidden by hide.py

optional arguments:
  -h, --help     show this help message and exit
  --input INPUT  Input picture file
 ``` 
