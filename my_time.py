from subprocess import call
import sys
import os
import time
from datetime import datetime
from screen_capture import ScreenCapture
from picture_ocr_read import OCRRead
from screen_text_array_format import ScreenTextMatrix
import thread

import PySimpleGUI27 as sg

#TODO: Using for potentialy GUI in the future
#sg.Popup('Welcome to MyTime!', 'Hopefully things will /timely/', 'Hahaha, I am so funny')


def get_file_name(command_args):
    # makes a default name for the files to be saved, based on date
    date_and_time = datetime.now()
    default_file_name = date_and_time.strftime("%B-%d-%Y--%I-%M-%S-%p")

    # if user doesn't input anything, files saved will use default_file_name
    file_name = default_file_name

    # Sees if user made a name for the file. If user types default, will use default_file_name
    if len(sys.argv) >= 2 and sys.argv[1].lower() != "default":
        file_name = command_args[1]

    return file_name

#names of the directories needed for the program
def create_files(screen_capture_dir, picture_ocr_read_dir, screen_text_array_format_dir):
    #Creates/checks for required directories for other programs
    if not os.path.isdir(screen_capture_dir):
        try:
            os.mkdir(screen_capture_dir)
            print("Made directory: " + screen_capture_dir)
        except OSError:
            print("Could not make folder: screen_shots")

    if not os.path.isdir(screen_text_array_format_dir):
        try:
            os.mkdir(screen_text_array_format_dir)
            print("Made directory: " + screen_text_array_format_dir)
        except OSError:
            print("Could not make folder: time_matrix")

    if not os.path.isdir(picture_ocr_read_dir):
        try:
            os.mkdir(picture_ocr_read_dir)
            print("Made directory: " + picture_ocr_read_dir)
        except OSError:
            print("Could not make folder: screen_text")

def input_thread(a_list):
    raw_input()
    a_list.append(True)


file_name = get_file_name(sys.argv)

screen_capture_dir = "./screen_shots/"
picture_ocr_read_dir = "./screen_text/"
screen_text_array_format_dir = "./time_matrix/"

create_files(screen_capture_dir, picture_ocr_read_dir, screen_text_array_format_dir)





current_iteration = 0

sc = ScreenCapture(title=file_name)

ocrr = OCRRead(title=file_name)
text_separator = ocrr.get_text_separator()

time_matrix = ScreenTextMatrix(title=file_name, text_separator=text_separator)


a_list = []
thread.start_new_thread(input_thread, (a_list,))
#currently just for testing
while not a_list:


    start_time = time.time()

    sc.take_screen_shot()
    ocrr.ocr_read()
    time_matrix.make_matrix()

    #makes sure it doesn't take screen shots more than every 10 seconds
    while time.time() - start_time < 10:
        time.sleep(.5)



    current_iteration += 1

print( current_iteration)


