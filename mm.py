#!/usr/bin/env python3
import random
import time

# Quartz ships with pyautogui on macOS (pyobjc-framework-Quartz). It's used directly
# because pyautogui.position() reads NSEvent.mouseLocation, which leaks ~48 bytes per call.
import Quartz

# Pixels moved per tick on each axis; the sign flips when an edge is reached
STEP_X = 1
STEP_Y = -1


def mouse_position():
    event = Quartz.CGEventCreate(None)
    loc = Quartz.CGEventGetLocation(event)
    return int(loc.x), int(loc.y)


def move_mouse(x, y):
    event = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (x, y), Quartz.kCGMouseButtonLeft)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)


def display_bounds(x, y):
    """Return (left, top, right, bottom) of the display containing (x, y), all inclusive."""
    err, ids, count = Quartz.CGGetDisplaysWithPoint((x, y), 1, None, None)
    display = ids[0] if err == 0 and count > 0 else Quartz.CGMainDisplayID()
    rect = Quartz.CGDisplayBounds(display)
    left, top = int(rect.origin.x), int(rect.origin.y)
    return left, top, left + int(rect.size.width) - 1, top + int(rect.size.height) - 1


def bounce(pos, step, low, high):
    """Advance pos by step within [low, high], inverting step when it would leave the range."""
    if not low <= pos + step <= high:
        step = -step
    return min(max(pos + step, low), high), step


def main():
    step_x, step_y = STEP_X, STEP_Y

    while True:
        x, y = mouse_position()
        left, top, right, bottom = display_bounds(x, y)
        x, step_x = bounce(x, step_x, left, right)
        y, step_y = bounce(y, step_y, top, bottom)
        move_mouse(x, y)
        print(f"mm: ({x}, {y})", flush=True)

        # Randomize the time to wait between 50 and 60 seconds
        time.sleep(random.randint(50, 60))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
