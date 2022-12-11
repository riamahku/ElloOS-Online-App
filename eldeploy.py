try:
    from datetime import datetime as d
    import numpy as np
    import perfplot, matplotlib
    from ast import Interactive
    print("AST Intercactive,              ..... OK")
    import os,sys,time,maskpass,keyboard
    print("os,sys,time,maskpass,keyboard, ..... OK")
    from colorama import Fore
    print("colorama fore,                 ..... OK")
    from colorama import Back
    print("colorama back,                 ..... OK")
    from colorama import Style
    print("colorama style,                ..... OK")
    import random, math
    print("random,math,                   ..... OK")
    import signal
    print("signal,                        ..... OK")
    import socket
    print("socket,                        ..... OK")
    import psutil
    print("psutil,                        ..... OK")
    from pyfiglet import figlet_format
    print("pyfiglet,                      ..... OK")
    from tqdm import tqdm
    print("tqdm,                          ..... OK")
except Exception:
    print(Fore.RED+"[IMPORT/FAIL]: Failed to import modules!")
    print("Restart your computer or check the bootfile!")
    os.system("pause")
    os.system("main.py")

console_local=0

os.system("cls")
def console():
    try:
        global console_local
        if console_local==0:
            print(Fore.CYAN+"(C) Copyright Ello Administrator Terminal")
            print(Fore.CYAN+"All reserved!")
        consoleInput = input(Fore.CYAN+"ADMINISTRATOR> ")
        console_local=1
        if consoleInput in("rst -i"):
            os.system("color 0f")
            os.system("cls")
            os.system("main.py")
        if consoleInput in("cls","clear","Cls","CLS","Clear","CLEAR"):
            os.system("cls")
            console_local=0
            console()
        if consoleInput in("-l1"):
            perfplot.show(
            setup=np.random.rand,
            kernels=[
            lambda a: np.c_[a, a],
            lambda a: np.stack([a, a]).T,
            lambda a: np.vstack([a, a]).T,
            lambda a: np.column_stack([a, a]),
            lambda a: np.cocatenate([a[:, None], a[:, None]], axis=1)
            ],
            labels=["c_","stack","vstack","column stack","concat"],
            n_range=[2 ** k for k in range(15)],
            xlabel="len(a)"
            )
            return
        if consoleInput in("Info","INFO","info"):
            print("Running application: ")
            for proc in psutil.process_iter(['name']):
                print(proc.info)
                time.sleep(.1)
            print(Fore.WHITE+"")
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
        if consoleInput in("dumpall"):
            msg = input("THIS SETTINGS MY BE DANGEROUS TO YOUR COMPUTER.")
            msg1 = input("FINAL WARNING MY BE DANGEROUS YOUR COMPUTER!")
            with open("dumpall.a","w") as e:
                e.write("dumpall (c)")
                e.close()

        if consoleInput in("get","GET","Get"):
            print(Fore.WHITE+"Loading...")
            getInput = input("$get> ")
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
    except Exception:
        console()
    finally:
        console()

console()
