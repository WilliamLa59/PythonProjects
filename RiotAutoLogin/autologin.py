import os
import time
import pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()

applocation = "app location"
username = "username"
password = "password"

os.startfile(applocation)

time.sleep(8)
keyboard.type(username)

keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.type(password)

keyboard.press(Key.enter)
keyboard.release(Key.enter)