# _*_ coding: utf-8 _*_
#/bin/bash

from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController


def main():
    keyboard = KeyboardController()
    mouse = MouseController()

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    sleep(0.35)

    mouse.press(Button.left)

    sleep(0.2)

    mouse.release(Button.left)

if __name__ == "__main__":
    main()
