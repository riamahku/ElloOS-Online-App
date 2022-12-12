import time,sys,os,rich
from rich.prompt import Prompt, Confirm

os.system("cls")
BOOTLOADER = True
BOOTFALSE = False
BOOTTRUE = True
BOOTSECTION = hex(1)

if BOOTLOADER == BOOTTRUE:
    print("Booting on SC1")

if BOOTLOADER == BOOTFALSE:
    pass

def quit_sys():
    sys.exit(0)

def load():
    os.system("main.py")

COPYRIGHT = "Copyright (c) SimpleBootloader V.1"
string = COPYRIGHT.center(20)
print(string)

loader = Prompt.ask("Enter 1 to 3", choices=["ElloOS", "Safemode","Administrator"],default="ElloOS")
if loader in("ElloOS"):
    os.system("main.py")
elif loader == "Safemode":
    os.system("safemode.py")
elif loader == "Administrator":
    os.system("eldeploy.py")