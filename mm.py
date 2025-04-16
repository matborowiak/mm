#!/usr/bin/env python3
import pyautogui
import time
import random

while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    # Move the mouse 1 pixel up
    pyautogui.moveTo(x, y - 1)
    # Print the new mouse position to the console
    print(f"mm: ({x}, {y - 1})")

    # Randomize the time to wait between 50 and 60 seconds
    time.sleep(random.randint(50, 60))