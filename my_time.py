from subprocess import call
import sys
import os
from datetime import datetime
from screen_capture import ScreenCapture
from picture_ocr_read import OCRRead
import PySimpleGUI27 as sg

#TODO: Using for potentialy GUI in the future
#sg.Popup('Welcome to MyTime!', 'Hopefully things will /timely/', 'Hahaha, I am so funny')

#makes a default name for the files to be saved, based on date
date_and_time = datetime.now()
default_file_name = date_and_time.strftime("%B-%d-%Y--%I-%M-%S-%p")

#if user doesn't input anything, files saved will use default_file_name
file_name = default_file_name

#Sees if user made a name for the file. If user types default, will use default_file_name
if len(sys.argv) >= 2 and sys.argv[1].lower() != "default":
    file_name = sys.argv[1]


#names of the directories needed for the program
screen_capture_dir = "./screen_shots"
picture_ocr_read_dir = "./screen_text"
screen_text_array_format_dir = "./time_matrix"


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


current_iteration = 0

sc = ScreenCapture(title=file_name)
ocrr = OCRRead(title=file_name)

while(current_iteration < 1):
    sc.take_screen_shot(current_iteration)
    ocrr.ocr_read(current_iteration)
    current_iteration += 1




#Calls the other programs
#call(["python", "screen_capture.py", file_name])
#call(["python", "picture_ocr_read.py", file_name])
#call(["python", "screen_text_array_format.py", file_name])
