import pyautogui
from pynput import keyboard
import time


def unlockDoor():
    pyautogui.moveTo(777, 835)
    # Click and drag to absolute coordinate (800, 500) over 1.5 seconds
    pyautogui.dragTo(600, 823, duration=1.5, button="left")

def lockDoor():
    pyautogui.moveTo(511, 828)
    # Click and drag to absolute coordinate (800, 500) over 1.5 seconds
    pyautogui.dragTo(687, 823, duration=1.5, button="left")


def on_press(key):

  try:
    # Regular alphanumeric keys (a-z, 0-9)
    print(f"Key pressed: {key.char}")
    if(key.char == "l"):
        print(pyautogui.position())
    if(key.char == "u"):
      unlockDoor()
    if(key.char == "c"):
      lockDoor()
    print("done")
  except AttributeError:
    
    #print(f"Special key pressed: {key}")
    pass


def on_release(key):
  
  if key == keyboard.Key.esc:
    print("Stopping keyboard listener...")
    return False





with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()

