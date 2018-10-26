import pyscreenshot as ImageGrab
from screeninfo import get_monitors
import time
import sys
from PIL import ImageFilter

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


print "Screen Capture... ",
sys.stdout.flush()




file_path = "./screen_shots/"
title = sys.argv[1]
file_type = ".png"

screen_width, screen_height = monitor_size()
screen_capture_rate_seconds = 3

current_seconds = int(time.time())
prev_5_second = 0
current_iteration = 0

'''
while(current_iteration < 5):
    if current_seconds%screen_capture_rate_seconds == 0 and prev_5_second != current_seconds:
        screen_shot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        screen_shot.save(file_path + title + str(current_iteration) + file_type)
        current_iteration += 1
        prev_5_second = current_seconds
    current_seconds = int(time.time())
    print(current_seconds)
'''

while(current_iteration < 1):
    screen_shot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    screen_shot = screen_shot.convert('L')
    #screen_shot = screen_shot.filter(ImageFilter.GaussianBlur(.5))
    screen_shot.save(file_path + title + "_" + str(current_iteration) + file_type)
    current_iteration += 1
    time.sleep(screen_capture_rate_seconds)


print("complete!")
sys.stdout.flush()