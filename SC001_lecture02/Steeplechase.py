"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    up()
    cross()
    down()


def turn_right():
    for i in range(3):
        turn_left()


def up():
    turn_left()
    while not right_is_clear():
        move()


def cross():
    turn_right()
    move()
    turn_right()
    move()


def down():
    while front_is_clear():
        move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
