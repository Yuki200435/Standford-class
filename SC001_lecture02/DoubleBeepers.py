"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_beepers_back()
    karel_go_home()


def double_beepers():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()


def put_beepers_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_left()
        turn_left()
        move()
        put_beeper()
        turn_left()
        turn_left()
        move()


def karel_go_home():
    turn_left()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
