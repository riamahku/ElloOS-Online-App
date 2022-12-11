import time,os
import curses
from colorama import Fore
with open("loader64.registry", "w") as f:
      f.write("loader64 EXT Bootloader x64VF")
      f.close()

button = ["ElloOS","Safemode"]
print("Running bootloader...")
time.sleep(2)
os.system("cls")

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(button):
        x = w//2 - len(row)//2
        y = h//2 - len(button)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    global current_row_idx
    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(button)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0, "Loading...{}".format(button[current_row_idx]))
            if button[current_row_idx] == "ElloOS":
                os.system("cls")
                os.chdir("..")
                os.remove("loader64.registry")
                os.chdir("..")
                os.system("main.py")
            if button[current_row_idx] == "Safemode":
                os.chdir("..")
                os.chdir("..")
                os.system("cls")
                os.system("safemode.py")
            stdscr.refresh()
            stdscr.getch()
        print_menu(stdscr,current_row_idx)
        stdscr.refresh()

curses.wrapper(main)
