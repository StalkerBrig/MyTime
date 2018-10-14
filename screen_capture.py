import pyscreenshot as ImageGrab
from screeninfo import get_monitors
import time

def monitor_size():
    get_monitors_str = str(get_monitors())

    letter_index = 0
    screen_width_str = ""
    screen_height_str = ""

    for letter_index in range(len(get_monitors_str)):
        if get_monitors_str[letter_index] == "(":
            letter_index += 1
            while(get_monitors_str[letter_index] != "x"):
                screen_width_str += get_monitors_str[letter_index]
                letter_index += 1
            letter_index += 1
            while(get_monitors_str[letter_index] != "+"):
                screen_height_str += get_monitors_str[letter_index]
                letter_index += 1
            break

    screen_width = int(screen_width_str)
    screen_height = int(screen_height_str)

    return screen_width, screen_height


file_path = "./screen_shots/"
title = "test_"
file_type = ".png"

screen_width, screen_height = monitor_size()

current_seconds = int(time.time())
current_iteration = 0
while(current_iteration < 10):
    if current_seconds%5 == 0:
        screen_shot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        screen_shot.save(file_path + title + str(current_iteration) + file_type)
        current_iteration += 1
    current_seconds = current_seconds = int(time.time())

