#!/usr/bin/env python

import os
import time
import sys
import pyautogui
from ctypes import Structure, windll, c_uint, sizeof, byref

print("It works~!")

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0



for i in range(30):
    print(get_idle_duration())
    time.sleep(1)

    if(get_idle_duration() >= 5):
        print(pyautogui.position())
        break;

