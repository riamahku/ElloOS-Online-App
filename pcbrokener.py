import os, sys, time

print("Waiting pc brokener...")
i = input("Do you want to destroy your pc? ")
if i in("yes","y","YES","Y","Yes"):
    pass
else:
    print("Cancelling pc brokener...")
    sys.exit(0)
i2 = input("Do you REALLY want to destroy your pc? ")
if i2 in("yes","y","YES","Y","Yes"):
    pass
else:
    print("Cancelling pc brokener...")
    sys.exit(0)

print("Your pc to be broken!!!")
os.remove("ElloOSBootsettings.ini")
os.remove("main.py")
os.remove("eldeploy.py")
print("Good Luck (: !")
