import pyscreenshot as ImageGrab
from screeninfo import get_monitors
import time
import sys
from PIL import ImageFilter
from PIL import Image

#Used for testing
MAX_ITERATION = 1

#Gets the size of the user's monitor
def monitor_size():
    get_monitors_str = str(get_monitors())

    screen_width_str = ""
    screen_height_str = ""

    #Parses the string with the monitor size; will get the width and height
    for letter_index in range(len(get_monitors_str)):

        # a '(' is the character right before the width
        if get_monitors_str[letter_index] == "(":
            #need to increase by 1 so it doesn't copy the '('
            letter_index += 1
            # 'x' is the character after the last number in the width
            while(get_monitors_str[letter_index] != "x"):
                #copys all numbers for width
                screen_width_str += get_monitors_str[letter_index]
                letter_index += 1

            #the character past the 'x' starts the heigth, so need to increase by 1
            letter_index += 1

            #the character past the height is '+', so loop until we hit the '+'
            while(get_monitors_str[letter_index] != "+"):
                #copys all numbers for height
                screen_height_str += get_monitors_str[letter_index]
                letter_index += 1

            #don't need anything else after this, so can break out loop
            break

    screen_width = int(screen_width_str)
    screen_height = int(screen_height_str)

    return screen_width, screen_height


print "Screen Capture... ",
sys.stdout.flush()

#TODO: Change this to accept argument value; using for MyMusicTime
MUSICTIME = False  # type: bool


file_path = "./screen_shots/"
title = sys.argv[1]
file_type = ".png"

#gets monitor size
screen_width, screen_height = monitor_size()

#TODO: Potentially change to higher/lower values
screen_capture_rate_seconds = 12

current_iteration = 0

#TODO: Will have to change this to some sort of interrupt; the user needs to determine when it stops
#TODO: Currently using iterations for test purposes
while(current_iteration < MAX_ITERATION):
    #gets a screenshot of user screen
    screen_shot_color = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))


    #Making the image bigger; helps the OCR read it
    screen_shot_color = screen_shot_color.resize((screen_width*2, screen_height*2), Image.NEAREST)
    #screen_shot_color = screen_shot_color.filter(ImageFilter.GaussianBlur(1.1))
    screen_shot_color.filter(ImageFilter.SHARPEN)

    #Converts to black white; easier for OCR readers
    screen_shot_bw = screen_shot_color.convert('L')

    #TODO: Use a blur? Not sure yet
    #screen_shot = screen_shot.filter(ImageFilter.GaussianBlur(.5))

    #saves screen shot to a file
    screen_shot_bw.save(file_path + title + "_" + str(current_iteration) + file_type, quality=300)

    #saves color screen shot for MyMusicTime
    if MUSICTIME == True:
        screen_shot_color.save(file_path + title + "_" + str(current_iteration) + file_type, quality=300)

    current_iteration += 1
    #sleeps process until a new screenshot is needed, based on screen_capture_rate

    if current_iteration == MAX_ITERATION-1:
        time.sleep(screen_capture_rate_seconds)


print("complete!")
sys.stdout.flush()