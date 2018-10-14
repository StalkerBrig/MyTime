try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import os.path
import re
import sys

print "Picture OCR Read... ",
sys.stdout.flush()


video_frame_name = sys.argv[1]
image_type = ".png"
video_seconds_name = video_frame_name + "_second_"
full_image_path = "video_frames/" + video_seconds_name

video_text_file = "video_text/"

movie_text_write = open(video_text_file+video_frame_name+".txt", "w")

sec = 0
while os.path.exists(full_image_path+"%d" % sec+image_type):
    if sec != 0:
        full_string = "\n\nzzzzzzzzzzzsecond: %d" % sec + "\n"
    else:
        full_string = "zzzzzzzzzzzsecond: %d" % sec + "\n"
    ocr_text = pytesseract.image_to_string(Image.open(full_image_path+"%d" % sec+image_type))
    parse_text = re.findall("[a-zA-Z]+", ocr_text)
    full_string += ' '.join(parse_text)
    full_string = full_string.lower()
    movie_text_write.write(full_string)

    sec += 1

movie_text_write.close()

print("complete!")
sys.stdout.flush()
