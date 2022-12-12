import os,requests,time,sys
from rich.prompt import Prompt, Confirm
from rich.progress import track
os.system("cls")

_OOBE = False
_FORCEINSTALLATION = False
_INSTALLER_RUN = True

#Confirm Installation
local = Confirm.ask("Do you want to install ElloOS? ")
if local == True:
    pass
else:
    print("Caceling installer...")
    time.sleep(2)
    sys.exit()

#Making dirs
print("Making directory...")
print(os.getcwd())
os.mkdir("Registry")
os.chdir("Registry")
f = open("ERRC.a", "w")
f.write("Registry Annsylator")
f.close()
os.mkdir("Bootloader")
os.chdir("..")
os.mkdir("usersDirectory")
print("Done making directory!")
print(os.getcwd())
for i in track(range(20),description="Processing direcotrys..."):
    time.sleep(.3)
#Beginning Installation ElloOS
print("Downloading ElloOS...")
main = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/main.py")
with open("main.py", "wb") as f:
    f.write(main.content)
    f.close()
print("Done download ElloOS")

#Beginning Installation regisMenu
print("Downloading REGISMENU V1...")
print(os.getcwd())
regisMenu = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/Registry/Bootloader/regisMenu.py")
time.sleep(5)
os.chdir("Registry")
os.chdir("Bootloader")
print("Making extension...")
f = open("loader64.loader", "w")
f.write("Loader64 Vers.1.0")
f.close()
f = open("dhcp-error.key", "w")
f.write(" ")
f.close()
print("Done, Registering REGISMENU...")
with open("regisMenu.py", "wb") as f:
    f.write(regisMenu.content)
    f.close()

print(os.getcwd())

#Changing directory to main directory
for i in range(2):
    os.chdir("..")
    time.sleep(.1)

#Beginning Installation fastboot
for i in track(range(21),description="Downloading Fastboot"):
    time.sleep(.2)
fastboot = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/fastboot.py")
with open("fastboot.py", "wb") as f:
    f.write(fastboot.content)
    f.close()

for i in track(range(21),description="Downloading BootSettings"):
    time.sleep(.2)
settings = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/ElloOSBootsettings.ini")
with open("ElloOSBootsettings.ini", "wb") as f:
    f.write(settings.content)
    f.close()

for i in track(range(21),description="Downloading FR"):
    time.sleep(.2)
fr = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/factory-reset.py")
with open("factory-reset.py", "wb") as f:
    f.write(fr.content)
    f.close()

for i in track(range(21),description="Downloading bootloader"):
    time.sleep(.2)
bl = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/bootloader.py")
with open("bootloader.py", "wb") as f:
    f.write(bl.content)
    f.close()

for i in track(range(21),description="Downloading eldeploy"):
    time.sleep(.2)
eldeploy = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/eldeploy.py")
with open("eldeploy.py", "wb") as f:
    f.write(eldeploy.content)
    f.close()

for i in track(range(21),description="Downloading ClientServer"):
    time.sleep(.2)
for i in track(range(21),description="Downloading ClietnServer V1"):
    time.sleep(.2)
server = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/serverstart.py")
client = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/clientstart.py")
with open("serverstart.py", "wb") as f:
    f.write(server.content)
    f.close()
with open("clientstart.py","wb") as f:
    f.write(client.content)
    f.close()

for i in track(range(21),description="Downloading safemode..."):
    time.sleep(.2)
safemode = requests.get("https://raw.githubusercontent.com/riamahku/ElloOS-Online-App/main/safemode.py")
with open("safemode.py","wb") as f:
    f.write(safemode.content)
    f.close()

print("Intializing Installer...")
if os.path.isfile("main.py"):
    print("Checked ElloOS Main")
if os.path.isfile("eldeploy.py"):
    print("Checked eldeploy")
if os.path.isfile("clientstart.py"):
    print("Checked clientstart")
if os.path.isfile("fastboot.py"):
    print("Checked fastboot")
if os.path.isfile("safemode.py"):
    print("Checked safemode")
if os.path.isfile("serverstart.py"):
    print("Checked serverstart")

for i in track(range(21),description="Processing installed apps..."):
    time.sleep(.2)

local = Confirm.ask("Do you want to reboot on SC1? ")
if local == True:
    _INSTALLER_RUN = False
    _OOBE = True
    _FORCEINSTALLATION = False
    os.system("bootloader.py")
else:
    try:
        _INSTALLER_RUN = False
        _OOBE = True
        _FORCEINSTALLATION = False
    except Exception:
        print("OOBE Falsed, connection github closed!")
