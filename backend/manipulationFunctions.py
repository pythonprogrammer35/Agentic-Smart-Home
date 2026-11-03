import pyautogui
from pynput import keyboard
import time


def unlockDoor():
    pyautogui.moveTo(525, 734)
    # Click and drag to absolute coordinate (800, 500) over 1.5 seconds
    pyautogui.dragTo(412, 725, duration=0.5, button="left")

def lockDoor():
    pyautogui.moveTo(258, 719)
    # Click and drag to absolute coordinate (800, 500) over 1.5 seconds
    pyautogui.dragTo(426, 731, duration=0.5, button="left")

def fanOn():
   pyautogui.click(567, 501)
   time.sleep(0.5)
   pyautogui.click(398, 646)
   time.sleep(0.5)
   pyautogui.click(518, 782)
   time.sleep(0.5)

def fanOff():
   pyautogui.click(565, 507)
   time.sleep(0.5)
   pyautogui.click(565, 507)
   time.sleep(0.5)
   pyautogui.click(394, 548)
   time.sleep(0.5)

"""def on_press(key):

  try:
    # Regular alphanumeric keys (a-z, 0-9)
    print(f"Key pressed: {key.char}")
    if(key.char == "l"):
        print(pyautogui.position())
    if(key.char == "u"):
      fanOn()
    if(key.char == "c"):
      fanOff()
    print("done")
  except AttributeError:
    
    #print(f"Special key pressed: {key}")
    pass


def on_release(key):
  
  if key == keyboard.Key.esc:
    print("Stopping keyboard listener...")
    return False





with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()"""

