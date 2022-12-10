import os,sys,time

#Very simple app uninstaller
print("Waiting app uninstaller...")
time.sleep(2)
print(os.system("dir"))
cls = input("Uninstall Item> ")
os.remove(cls)
os.system("AppUninstaller.py")
