#Check bootable devices!
import os
print("Checking currrent directory...... OK "+os.getcwd())
os.chdir("Registry")
if not os.path.isfile("loader64.registry"):
    os.system("cls")
    print(os.getcwd())
    os.chdir("Bootloader")
    os.system("regisMenu.py")
    os.chdir("..")

os.chdir("..")
os.system("cls")
print("Intializing modules, Don't turn off your computer")
from colorama import Back
from colorama import Style
from colorama import Fore
import speedtest
import numpy as np
from datetime import datetime as d
from ast import Interactive
import wmi
import curses
from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.progress import track
from rich.traceback import install
import sys,time,maskpass,keyboard
import socket
from scapy.all import *
import random, math
import signal
import socket
import psutil
from pyfiglet import figlet_format
from tqdm import tqdm
from os import getcwd
import requests

st = speedtest.Speedtest()
console = Console()
locales = random.randint(1,2)
try:
    print("Done")
    for i in track(range(locales),description="Intializing Boot Manager"):
        time.sleep(locales)
except Exception:
    print("[IMPORT/FAIL]: Failed to import modules!")
    os.system("pause")
    os.system("main.py")
time.sleep(5)
console_local=0
global defaultos
defaultos = "Ello"
install()
def boottab():
    os.system("cls")
    print(Fore.WHITE+"|GENERAL|BOOT|EXIT|")
    print("waiting wmic")
    print("Current booting on: ")
    os.system("wmic diskdrive get model,serialNumber,size,mediaType")

done = 'false'
#here is the animation
def animate():
    while done == 'false':
        sys.stdout.write('\rLOCAL: |')
        time.sleep(0.3)
        sys.stdout.write('\rLOCAL: /')
        time.sleep(0.3)
        sys.stdout.write('\rLOCAL: -')
        time.sleep(0.3)
        sys.stdout.write('\rLOCAL: \\')
        time.sleep(0.3)
    sys.stdout.write('\rDone!     ')
#long process here
done = 'false'

def permanent_error():
    os.system("cls")
    os.system("color 0f")
    print("System has been halted, Your computer is on non-biosmode, the computer permaently errors!")
    print("Error Code: BOOTFILE_NOT_FOUND")
    animate()

if os.path.isfile("dumpall.a"):
    permanent_error()

def progress_bar(progress, total):
    percent = 100*(progress/float(total))
    bar = '█'*int(percent)+'-'*(100-int(percent))
    print(f"\r|{bar}| {percent:.2f}%",end="\r")

numbers = [x*5 for x in range(2000,3000)]
results = []

def ip_checker():
    for i in track(range(15),description="Loading..."):
        pass
    os.system("cls")
    print(Fore.WHITE+"Starting IpChecker")
    print(figlet_format("IpChecker",font="standard"))
    print(Fore.CYAN+"A> Check ethernet info")
    print(Fore.CYAN+"B> Check IP")
    print(Fore.CYAN+"C> EXIT")
    while True:
        if keyboard.is_pressed("a"):
            print(Fore.WHITE+"")
            ethernet_info = Ether()
            ethernet_show = ethernet_info.show()
            print(ethernet_show)
            os.system("pause")
            ip_checker()

        if keyboard.is_pressed("b"):
            ip_info = ip()
            ip_show = ip_info.show()
            print(ip_show)
            os.system("pause")
            ip_checker()

        if keyboard.is_pressed("c"):
            print("Restarting")
            os.system("main.py")


def check_root():
    os.system("cls")
    if not os.path.isfile("main.py"):
        permanent_error()
    if __name__ == __name__:
        print("Done rooting device... CHECKING...")
    else:
        print("Failed rooting device... CHECKING...")
    time.sleep(2)
    print("Checking Boot File...")
    if os.path.isfile("ElloOSBootsettings.ini"):
        print("Pass, No error found")
    else:
        try:
            with open("ElloOSBootsettings.ini","r") as f:
                read_file_content = f.read()
                for i in read_file_content:
                    print(i)
        except IOError:
             print(Fore.RED+"[IOError]: Failed reading bootfile, please repair the bootfile to continue!")
             print(Fore.BLUE+"[INFO/OS]: If you're done repairing restart the computer!")
             os.system("pause")
             os.system("main.py")
    time.sleep(2)
    print("Checking computer name...")
    try:
        print(os.name())
    except Exception:
        print(Fore.RED+"[EXCEPTION]: Cannot read computer name/versions ... Skipping...")
        print(Fore.WHITE+" ")

    print("Checking packages manager...")
    print("Setting up current directory....")
    path = os.getcwd()
    founds = os.listdir(path)
    for i in founds:
        pass
    print("Has been found: ",i)
    print("Checking...")
    if founds == 'toolmanager':
        print("Founded toolmanager!")
    print("Done checking, Beginning to Operating System...")
    os.system("pause")

def bootRepair():
    os.system("cls")
    os.system("color 1f")
    print("                        ElloOS Repair")
    for i in tqdm(range(int(9e5)),ncols=120,desc="Repairing your computer...."):
        pass
    for i in range(53):
        os.system("cls")
        print("Dumping your files:",i)
    try:
        os.remove("ERRC.a")
    except FileNotFoundError:
        print(Fore.RED+"[OS/ERROR]: Cannot remove the ERRC.a on ",os.getcwd()+" The system to be halted!")
        try:
            print("Trying to remove again...")
            os.remove("ERRC.a")
        except FileNotFoundError as Error:
            print(Fore.RED+"[OS/ERROR]: Cannot remove!, DRCT at ",Error," and on ",os.getcwd()," directory!")
            time.sleep(2)
            permanent_error()
    if not os.path.isfile("ElloOSBootsettings.ini"):
        try:
            with open("ElloOSBootsettings.ini",'w') as f:
                f.write("BACKUPS STARTUP.../// RUN ON \\BACKUP")
                f.close()
            os.system("main.py")
        except Exception:
            permanent_error()

        try:
            os.rename("localdata","ElloOSBootsettings.ini")
        except Exception:
            permanent_error()
    for i in tqdm(range(int(9e4)),ncols=120,desc="Checking .lib"):
        pass
    for i in tqdm(range(int(9e6)),ncols=120,desc="Checking .src"):
        pass
    for i in tqdm(range(int(9e5)),ncols=120,desc="Checking .usersDirectory"):
        pass
    for i in tqdm(range(int(9e4)),ncols=120,desc="Restarting your device"):
        pass
    time.sleep(1)
    os.system("color 0f")
    os.system("main.py")

def bluescreen():
    os.system("cls")
    os.system("color 1f")
    print("                        ELLOOS Terminated")
    print("Your computer has been shutdown automatically")
    print("because your computer has a problem and need to repair it")
    print("*Press any key to restart the system!")
    os.system("pause")
    bootRepair()

if os.path.isfile("ERRC.a"):
    bluescreen()
if not os.path.isfile("ElloOSBootsettings.ini"):
    with open("ERRC.a","w") as f:
        f.write("Error bootini")
        f.close()
    bluescreen()

FORMAT = 'utf-8'
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def terminal_send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def term_mt():
    term = input("FSTBT_INET> ")
    terminal_send(term)
    if term in("rst -bt"):
        print("The fast boot was closed!")
        print("Waiting to restart...")
        os.system("cls")
        os.system("main.py")
    elif term in("patch"):
        patch = input("What do you want to patch?: ")
        if patch in("A:/","a:/","a"):
            print("patching on A:/...")
            terminal_send("Terminal disconnected")
    term_mt()

def fstbt_shell():
    PORT = input("Input the port to connect: ")
    PORT = int(PORT)
    dc_msg = "Terminal disconnected"
    SERVER = input("Input the IP: ")
    ADDR = (SERVER, PORT)
    client.connect(ADDR)
    term_mt()
def tool():
    os.system("cls")
    if not os.path.isfile("toolmanager"):
        print(Fore.RED+"Cannot start toolmanager, Error: [Not find tool manager file]")
        os.system("pause")
        os.system("main.py")
    else:
        pass

    print(Fore.WHITE+"Starting tool manager...")
    print(figlet_format("Tool Mgr",font="standard"))
    print(Fore.CYAN+"A> Show all statistic from computer")
    print(Fore.CYAN+"B> Close Tool Manager")
    print(Fore.CYAN+"C> About Tool Manager")
    while True:
        if keyboard.is_pressed("a"):
          print(Fore.WHITE+"CPU Percent: ")
          for i in range(5):
              print(psutil.cpu_percent(interval=1))

          print(Fore.WHITE+"CPU Frequency: ")
          print(psutil.cpu_freq())

          time.sleep(5)
          print(Fore.WHITE+"Net IO: ")
          print(psutil.net_io_counters(pernic=True))

          time.sleep(2)
          message = "Tool.exe has been flushed, the system will be restarted!."
          for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.1)
        if keyboard.is_pressed("b"):
          os.system("main.py")

        if keyboard.is_pressed("c"):
          os.system("cls")
          print(Fore.WHITE+"Tool Manager is a tool to see the system management for realtime!")
          print(Fore.WHITE+"(C) Copyright Tool Manager 2021-2022")
          time.sleep(2)

          os.system("main.py")


def console():
    global console_local
    if console_local==0:
        print(Fore.CYAN+"(C) Copyright Ello Terminal")
        print(Fore.CYAN+"All reserved!")
    consoleInput = input(Fore.CYAN+"> ")
    console_local=1
    if consoleInput in("cls","clear","Cls","CLS","Clear","CLEAR"):
        os.system("cls")
        console_local=0
        console()
    if consoleInput in("Info","INFO","info"):
        print("Running application: ")
        for proc in psutil.process_iter(['name']):
            print(proc.info)
            time.sleep(.1)
        print(Fore.WHITE+"")
        console()
    if consoleInput in("fstbt -i shell"):
        fstbt_shell()
    if consoleInput in("pkts"):
        while True:
            print(psutil.net_io_counters(pernic=False))
            time.sleep(.1)
            os.system("cls")
    if consoleInput in("fastboot -i"):
        fstboot = input("Do you want to enter fasboot? [Y/n]: ")
        if fstboot in("y","Y","yes","Yes","YES"):
            print("Loading fastboot...")
            os.system("fastboot.py")
    if consoleInput in("speedtest"):
        choice = input('''1.Download speed
                          2.Upload speed
                          3.Ping

                          Choice: ''')
        if choice in("1"):
            print("Dowload speed: ")
            for i in range(5):
                print(int(st.download()))
            console()

        elif choice in("2"):
            print("Upload speed: ")
            for i in range(5):
                print(st.upload())
            console()

        elif choice in("3"):
            servername = []
            st.get_servers(servername)
            for i in range(5):
                print(st.results.ping)
            console()
        else:
            print("please insert correct choice!")
    if consoleInput in("reset","RESET","Reset"):
        print("Please select your selection!")
        print("1> Factory Reset")
        print("2> Reset system")
        rst = input("?> ")
        if rst in("1"):
            #Factory RESET
            pin = input("Input pin: ")
            if pin in("0000"):
                pass
            else:
                print("Wrong pin!")
                console()
            URC = input("Do you really want to factory reset? [Y/n]: ")
            if URC in("yes","YES","Yes","y","Y"):
                os.system("factory-reset.py")
            else:
                console()

    if consoleInput in("ipconfig","IPCONFIG","Ipconfig"):
        host_name = socket.gethostname()
        ilocal = socket.gethostbyname(host_name)
        print(Fore.CYAN+"IPCONFIG")
        print(Fore.WHITE+"HOST NAME......."+host_name)
        print("LOCAL IP........"+ilocal)
        console()
    if consoleInput in("echo","ECHO","Echo"):
        echo = input(" ->")
        print(Fore.BLUE+echo)
        console()
    if consoleInput in("check","Check","CHECK"):
        check_root()
    if consoleInput in("run"):
        run = input(Fore.WHITE+"Run a specific files: ")
        if run in("tool","Tool","TOOL"):
            tool()
        if run in("ipchecker"):
            ip_checker()
    if consoleInput in("client start"):
        os.system("clientstart.py 192.168.1.16 4444")
    if consoleInput in("server start","Server Start","Server start","serverstart","SERVERSTART"):
      print("Please wait...")
      print("Running in...")
      os.system("serverstart.py 192.168.1.16 4444")
      if consoleInput in("exit","EXIT","Exit"):
        os.system("cls")
        os.system("main.py")

    if consoleInput in("admin","Admin","ADMIN"):
      try:
          with open("admin.ini","w") as f:
              f.write("administrator_write_only")
              f.close()
          print(Fore.GREEN+"[SUCSESS]: Sucsessfully set users to admin!")
          print(Fore.WHITE+" ")
          time.sleep(2)
          console()
      except Exception:
            print(Fore.RED+"[EXCEPT]: Error to make users to admin!")
            print(Fore.WHITE+" ")
    if consoleInput in("rename","Rename","RENAME"):
        main = input("Rename file: ")
        if main in("bootfile.ini"):
            main1 = input("Do you want to rename sesitive files?: [Y/n]: ")
            if main1 in("yes","YES","Yes"):
                if os.path.isfile("admin.ini"):
                    fd = 'ElloOSBootsettings.ini'
                    main3 = input("Rename file name: ")
                    os.rename(fd,main3)
                    print(Fore.GREEN+"[SUCSESS]: Sucsessfully changes!")
                    print(Fore.WHITE+" ")
                    os.system("pause")
                    console()
                else:
                    print(Fore.RED+"[ERROR/EXCEPTION]: Users are not allowed changes sensitive .ini files!")
                    print(Fore.WHITE+" ")
                    os.system("pause")
                    console()
            else:
                console()
    if consoleInput in("delete","Delete","DELETE"):
        os.system("dir")
        menuDel = input("Delete files: ")
        try:
            os.remove(menuDel)
            console()
        except Exception:
            print(Fore.RED+"[EXCEPTION]: Cannot delete files!")
            console()
    if consoleInput in("python"):
        os.system("cls")
        os.system("python")

    if consoleInput in("get","GET","Get"):
        print(Fore.WHITE+"Loading...")
        getInput = input("$get> ")
        if getInput in("cpython"):
            print("Auto-Finding...")
            print("Getting on github...")
            re1 = requests.get("https://raw.githubusercontent.com/python/cpython/main/Lib/os.py")
            with open("cpython.py", "wb") as f:
                f.write(re1.content)
                f.close()
            inpt = input("Run new OS now? ")
            if inpt in("yes","YES","Yes","Y","y"):
                os.system("cpython.py")
            else:
                console()
        if getInput in("appuninstaller"):
            print("Auto-Finding...")
            print("Getting on github please wait...")
            re = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/AppUninstaller.py?token=GHSAT0AAAAAAB4HVQK3KU34O6XPMGDKRZDAY4VGTYA")
            with open("appuninstaller.py", "wb") as f:
                f.write(re.content)
            rune = input("Do you want to run this program? [Y/n]: ")
            if rune in("yes","YES","Yes","y","Y"):
                os.system("appuninstaller.py")
            else:
                console()
        if getInput in("pcbrokener"):
            print("Auto-Finding...")
            print("Getting on github please wait...")
            r = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/pcbrokener.py?token=GHSAT0AAAAAAB4HC7QK7SV7NVV3HYISCAP2Y4VDOWA")

            with open("pcbrokener.py", "wb") as f:
                f.write(r.content)
            run = input("Do you want to run this program? [Y/n]: ")
            if run in("yes","YES","Yes","y","Y"):
                os.system("pcbrokener.py")
            else:
                console()
        if getInput in("ipchecker"):
            print("Auto-finding....")
            time.sleep(2)
            with open("ipchecker",'w') as f:
                f.write("IPCHECKER <C>")
                f.close()
            ip_checker()
        if getInput in("tool"):
            print(Fore.WHITE+"Getting information from tool...")
            print("Waiting  tool manufacturing")
            if os.path.isfile("toolmanager"):
                b = os.path.getsize("toolmanager")
            else:
                b = os.path.getsize("ElloOSBootsettings.ini")
            file = os.path.getsize("ElloOSBootsettings.ini")

            progress_bar(0,len(numbers))
            for i, x in enumerate(numbers):
                results.append(math.factorial(x))
                progress_bar(i+1,len(numbers))
            for i in tqdm(range(int(file)),ncols=90,desc="Finalizing..."):
                pass
            try:
                if not os.path.isfile("toolmanager"):
                    print("Downloading tool...")
                    with open("toolmanager","w") as f:
                      f.write("Tool manufacturer Inplementation, Succsess downloading TooL")
                      f.close()
                    print(Fore.GREEN+"Done, Downloading Tool!")
                else:
                    print(Fore.GREEN+"File already downloaded!")
                    console()

            except Exception as e:
                print(Fore.RED+f"Problem with managing file, Error: {e}")

            console()

def control_panel():
    os.system("cls")
    print(Fore.BLUE+"> Control Panel")
    print(Fore.WHITE+" ")
    print("1> Reset accounts")
    while True:
        if keyboard.is_pressed('1'):
            print(Fore.CYAN+"> Deleting users directory...")
            os.remove("usersDirectory/username.txt")
            os.remove("usersDirectory/password.txt")
            time.sleep(2)
            os.rmdir("usersDirectory")
            time.sleep(2)
            print(Fore.WHITE+" ")
            os.system("cls")
            os.system("main.py")


def shut_down():
    os.system("cls")
    print(Fore.RED+"> Shutting Down System...")
    time.sleep(2)
    sys.exit(1)

def window_start():
    os.system("cls")
    print(Fore.GREEN+"? What you want to do ?")
    print(Fore.WHITE+" ")
    print("a> Shut down")
    print("b> Control panel")
    print("c> Console")
    keyboardinput=True
    while keyboardinput:
        if keyboard.is_pressed('a'):
            shut_down()
            keyboardinput=True

        elif keyboard.is_pressed('b'):
            control_panel()
            keyboardinput=True

        elif keyboard.is_pressed('c'):
            os.system("cls")
            console()
            keyboardinput=True

def start():
    print("Starting ElloOS...")
    if not os.path.isdir("usersDirectory"):
        try:
          os.mkdir("usersDirectory")
          print("Sucsessfully making Users Directory")
        except Exception as e:
          print(f"Error {e}.")

    if not os.path.isfile("usersDirectory/username.txt"):
        username = input("Input your username: ")
        password = maskpass.askpass(mask="")
        linesUsername = [username]
        linesPassword = [password]
        try:
            with open("usersDirectory/username.txt",'w') as f:
                f.writelines(linesUsername)

            with open("usersDirectory/password.txt",'w') as f:
                f.writelines(linesPassword)
        except Exception as e:
            print(f"Error on {e}.")
    print(f"Done making file!")
    window_start()

print("Starting ElloOS...")
try:
    start()
except KeyboardInterrupt:
    os.system("cls")
    print("Has been Interrupted the interpreter")
    print("Launching python...")
    time.sleep(2)
    print(Fore.WHITE+"")
    os.system("cls")
    os.system("eldeploy.py")
curses.wrapper(main)
