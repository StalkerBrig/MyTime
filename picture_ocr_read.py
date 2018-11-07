try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import os.path
import re
import sys
import time

print "Picture OCR Read... ",
sys.stdout.flush()


screen_frame_name = sys.argv[1]
image_type = ".png"
screen_iteration_name = screen_frame_name + "_"
full_image_path = "screen_shots/" + screen_iteration_name

screen_text_file = "screen_text/"

#writes text from screen shot to this file
screen_text_write = open(screen_text_file+screen_frame_name+".txt", "w")

iteration = 0

#TODO: Will need to change this based on when screen capture is actually done, since there can be potential delays
#goes through the screenshots being taken
while os.path.exists(full_image_path+"%d" % iteration+image_type):

    start_time = time.time()

    #just formatting based on if it is the first (0th) iteration or not. Don't need the \n\n, since no text is above
    # the first iteration
    if iteration == 0:
        #This is just used as an easier way to parse data, based on interations
        full_string = "zzzzzzzzzzziteration: %d" % iteration + "\n"
    else:
        #This is just used as an easier way to parse data, based on interations
        full_string = "\n\nzzzzzzzzzzziteration: %d" % iteration + "\n"

    #convert image to text
    ocr_text = pytesseract.image_to_string(Image.open(full_image_path+"%d" % iteration+image_type))
    #Only keeping text/letters that are between letters a-z; including capitals.
    # Numbers aren't included, they don't currently seem necessary
    parse_text = re.findall("[a-zA-Z]+", ocr_text)

    #puts the parsed info into one big string, separated by spaces
    full_string += ' '.join(parse_text)

    #lower all words in string so we don't have multiple entries for same word, different capitalization
    # ex: "Moon", "moon", "mOOn" should all be seen as the same word
    full_string = full_string.lower()

    #writes to file
    screen_text_write.write(full_string)

    iteration += 1

    end_time = time.time()

    print("TIME TAKEN: ", end_time - start_time)

screen_text_write.close()

print("complete!")
sys.stdout.flush()
