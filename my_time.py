from subprocess import call
import sys

video_file_name = sys.argv[1]

call(["python", "video_frame_reduce.py", video_file_name])
call(["python", "picture_ocr_read.py", video_file_name])
call(["python", "video_text_array_format.py", video_file_name])
