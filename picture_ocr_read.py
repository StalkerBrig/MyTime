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


screen_frame_name = sys.argv[1]
image_type = ".png"
screen_iteration_name = screen_frame_name + "_"
full_image_path = "screen_shots/" + screen_iteration_name

screen_text_file = "screen_text/"

movie_text_write = open(screen_text_file+screen_frame_name+".txt", "w")

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
    movie_text_write.write(full_string)

    iteration += 1

movie_text_write.close()

print("complete!")
sys.stdout.flush()
