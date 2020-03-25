# _*_ coding: utf-8 _*_
#/bin/bash

import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller
from time import sleep

COMBINATIONS = [
    {keyboard.Key.alt_l, keyboard.KeyCode(char='z')}
]

current = set()

keeb = Controller()

def execute():
    #pyautogui.press('enter')
    print('nut')
    keeb.press(Key.enter)
    sleep(0.2)
    keeb.release(Key.enter)
    

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
