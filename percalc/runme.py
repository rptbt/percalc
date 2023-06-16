#!/usr/bin/python3

from math import *
import curses
from curses import wrapper

def configure():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    return stdscr

def calcmain(stdscr):
    num_enters = 0
    num_lines = curses.LINES-1
    num_cols = curses.COLS-1
    title = "Persistent Python Calculator: Type calculation and Press Enter"
    warning = "WARNING: This package WILL execute arbitrary code if you ask it nicely ;)"
    stdscr.addstr(0,0, title) #"Persistent Python Calculator: Type calculation and Press Enter")
    stdscr.addstr(1,0, warning, curses.A_REVERSE)#"WARNING: This package WILL execute arbitrary code if you ask it nicely ;)", curses.A_REVERSE)
    stdscr.addstr(num_lines, 0, "Esc to exit", curses.A_REVERSE)
    stdscr.refresh()
    #Move the cursor to line 3,0 to start
    last_curs_start_y, last_curs_start_x = (3,0)
    stdscr.move(3,0)
    string_buffer = ""
    while(1):
        #if current character is 'Enter', capture the line
        #elif current character is'Home', close down
        
        c = stdscr.getch()
        if c == curses.KEY_ENTER or c == 10 or c==13:
            pass_paren_lint = True
            if string_buffer != "" and pass_paren_lint:
                stdscr.addstr(num_lines-1, 0, "{}".format(string_buffer))
                res = eval(string_buffer.replace("^", "**"))
            stdscr.addstr(last_curs_start_y+1, last_curs_start_x+1, "String Buffer: {} Result: {}".format(string_buffer, res))
            stdscr.refresh()
            if last_curs_start_y + 3 >= num_lines or last_curs_start_x +3 >= num_cols:
                stdscr.clear()
                stdscr.addstr(0,0, title) #"Persistent Python Calculator: Type calculation and Press Enter")
                stdscr.addstr(num_lines, 0, "Esc to exit", curses.A_REVERSE)
                stdscr.addstr(3, 0, string_buffer)
                stdscr.addstr(4,0, "Result: {}".format(eval(string_buffer.replace("^", "**"))))
                stdscr.move(6,0)
                stdscr.refresh()
                last_curs_start_y = 6
                last_curs_start_x = 0
            else:
                stdscr.move(last_curs_start_y+3,0)
                stdscr.refresh()
                last_curs_start_y += 3
            string_buffer = ""
         
        elif c == 0x1b:
            break
        elif c in (curses.KEY_BACKSPACE, '\b', 127, 263):
            string_buffer = string_buffer[:-1]
        else:
            string_buffer += (chr(c))
        stdscr.addstr(num_lines-1, 0, "Last Character interpreted as {}".format(c))
        stdscr.move(last_curs_start_y,last_curs_start_x)
        stdscr.refresh()
        
    return


def main():
    st= configure()
    curses.wrapper(st, calcmain(st))
    curses.nocbreak()
    st.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    main()
