from subprocess import call
import sys
import os

file_name = sys.argv[1]

try:
    os.mkdir("./screen_shots")
except OSError:
    print("Could not make folder: screen_shots")

try:
    os.mkdir("./time_matrix")
except OSError:
    print("Could not make folder: time_matrix")

try:
    os.mkdir("./image_text")
except OSError:
    print("Could not make folder: image_text")


#call(["python", "video_frame_reduce.py", video_file_name])
call(["python", "screen_capture.py", file_name])
call(["python", "picture_ocr_read.py", file_name])
call(["python", "video_text_array_format.py", file_name])
