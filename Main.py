import os
from time import sleep
from app import tkwindows
test = 1
STOREOK = False
process = 0

tkwindows.buttons()
try:
    os.system("attrib 1 -h")
    os.system("rmdir 1 /s /q")
except:
    raise
os.system("mkdir 1")
os.system("attrib 1 +h")
tkwindows.root.mainloop()