import os
print("Removing on "+os.getcwd())
print("Removing registry")
os.chdir("Registry")
os.remove("ERRC.a")
os.chdir("Bootloader")
os.remove("dhcp-error.key")
os.remove("loader64.loader")
os.remove("loader64.registry")
os.remove("regisMenu.py")
os.chdir("..")
os.rmdir("Bootloader")
os.chdir("..")
os.rmdir("Registry")
os.chdir("usersDirectory")
os.remove("username.txt")
os.remove("password.txt")
os.chdir("..")
os.rmdir("usersDirectory")
print("Removing components...")
os.remove("clientstart.py")
os.remove("eldeploy.py")
os.remove("ElloOSBootsettings.ini")
os.remove("fastboot.py")
os.remove("main.py")
os.remove("safemode.py")
os.remove("serverstart.py")
if os.path.isfile("toolmanager"):
    os.remove("toolmanager")
else:
    pass
if os.path.isfile("ipchecker"):
    os.remove("ipchecker")
else:
    pass
if os.path.isfile("appuninstaller.py"):
    os.remove("appuninstaller.py")
else:
    pass
if os.path.isfile("pcbrokener.py"):
    os.remove("pcbrokener.py")
else:
    pass
print("Done removing!")
os.system("Installer.py")
