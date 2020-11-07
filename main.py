# Cps-Booster For Getting High Cps While PLaying Minecraft For Bridging And PvP 
# If You Like This Script Then Please Follow Me on Github --> www.github.com/harish795

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from keyboard import is_pressed as key_press
from json import load
from sys import exit as sry_exit
import time
import threading
import ctypes

try:
	# Opening settings File
	settings = open("settings.json",)
	data = load(settings) 
except:
    print('Sorry "settings.json" is required to use this script. If you havent downloaded the file with this script then try downloading it by this url --> "https://github.com/Harish795/CPS-Booster" keep both main.py" and "settings.json" in one folder')
    print("Press 'Esc' To Exit")
    while True:
        if key_press('Esc'):
            print("Exiting...")
            sry_exit() 

delay_for_right_mouse = data['delay_for_right_mouse']
delay_for_left_mouse = data['delay_for_left_mouse']
start_and_stop_key_for_left_button = KeyCode(char=data['start_and_stop_key_for_left_button'])
start_and_stop_key_for_right_button = KeyCode(char=data['start_and_stop_key_for_right_button'])
exit_key = KeyCode(char=data['exit_key'])

#print(data['delay_for_right_mouse'])z

class Clicker(threading.Thread):
    def __init__ (self, delay_for_right_mouse, delay_for_left_mouse):
        super(Clicker, self).__init__()
        self.delay_for_right_mouse = delay_for_right_mouse
        self.delay_for_left_mouse = delay_for_left_mouse
        self.running_left = False
        self.running_right = False
        self.program_running = True

    def start_clicking_left(self):
        self.running_left = True

    def stop_clicking_left(self):
        self.running_left = False

    def start_clicking_right(self):
        self.running_right = True

    def stop_clicking_right(self):
        self.running_right = False

    def exit(self):
        self.stop_clicking_left()
        self.stop_clicking_right()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running_left:
                mouse.click(Button.left)
                time.sleep(delay_for_left_mouse)
            time.sleep(0.1)
            while self.running_right:
                mouse.click(Button.right)
                time.sleep(delay_for_right_mouse)
            time.sleep(0.1)

mouse = Controller()
click_thread = Clicker(delay_for_right_mouse, delay_for_left_mouse)
click_thread.start()


def on_press(key):
    if key == start_and_stop_key_for_left_button:
        if click_thread.running_left:
            click_thread.stop_clicking_left()
        else:
            click_thread.start_clicking_left()
    elif key == start_and_stop_key_for_right_button:
        if click_thread.running_right:
            click_thread.stop_clicking_right()
        else:
            click_thread.start_clicking_right()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

