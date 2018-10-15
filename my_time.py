from subprocess import call
import sys
import os

file_name = sys.argv[1]

screen_capture_dir = "./screen_shots"
picture_ocr_read_dir = "./screen_text"
screen_text_array_format_dir = "./time_matrix"


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


#call(["python", "video_frame_reduce.py", video_file_name])
call(["python", "screen_capture.py", file_name])
call(["python", "picture_ocr_read.py", file_name])
call(["python", "screen_text_array_format.py", file_name])
