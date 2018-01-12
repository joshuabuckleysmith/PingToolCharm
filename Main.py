import os
from app import tkwindows

test = 1
STOREOK = False
process = 0

print("welcome to ping")

os.system("IF NOT EXIST 1 mkdir 1")
os.system("attrib 1 +h")
tkwindows.buttons()


tkwindows.root.mainloop()
