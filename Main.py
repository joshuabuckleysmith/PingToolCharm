import os
from app import tkwindows
test = 1
STOREOK = False
process = 0

os.system("IF EXIST 1 attrib 1 -h /s > nul")
os.system("IF EXIST 1 rmdir 1 /s /q > nul")
os.system("mkdir 1")
os.system("attrib 1 +h")
tkwindows.buttons()
tkwindows.root.mainloop()