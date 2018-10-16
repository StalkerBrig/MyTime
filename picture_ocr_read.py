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


#TODO: https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

screen_frame_name = sys.argv[1]
image_type = ".png"
screen_iteration_name = screen_frame_name + "_"
full_image_path = "screen_shots/" + screen_iteration_name

screen_text_file = "screen_text/"

screen_text_write = open(screen_text_file+screen_frame_name+".txt", "w")

iteration = 0
while os.path.exists(full_image_path+"%d" % iteration+image_type):
    if iteration != 0:
        full_string = "\n\nzzzzzzzzzzziteration: %d" % iteration + "\n"
    else:
        full_string = "zzzzzzzzzzziteration: %d" % iteration + "\n"
    ocr_text = pytesseract.image_to_string(Image.open(full_image_path+"%d" % iteration+image_type))
    parse_text = re.findall("[a-zA-Z]+", ocr_text)
    full_string += ' '.join(parse_text)
    full_string = full_string.lower()
    screen_text_write.write(full_string)

    iteration += 1

screen_text_write.close()


'''
screen_frame_name = sys.argv[1]
image_type = ".png"
screen_iteration_name = screen_frame_name + "_"
full_image_path = "screen_shots/" + screen_iteration_name

screen_text_file = "screen_text/"

screen_text_write = open(screen_text_file+screen_frame_name+".txt", "w")

iteration = 0

import pyocr
import pyocr.builders
from PIL import Image

while os.path.exists(full_image_path+"%d" % iteration+image_type):
    if iteration != 0:
        full_string = "\n\nzzzzzzzzzzziteration: %d" % iteration + "\n"
    else:
        full_string = "zzzzzzzzzzziteration: %d" % iteration + "\n"
    tools = pyocr.get_available_tools()[0]
    ocr_text = tools.image_to_string(Image.open(full_image_path+"%d" % iteration+image_type))
    #ocr_text = pytesseract.image_to_string(Image.open(full_image_path+"%d" % iteration+image_type))
    builder = pyocr.builders.TextBuilder
    parse_text = re.findall("[a-zA-Z]+", ocr_text)
    full_string += ' '.join(parse_text)
    full_string = full_string.lower()
    screen_text_write.write(full_string)

    iteration += 1

screen_text_write.close()
'''



print("complete!")
sys.stdout.flush()
