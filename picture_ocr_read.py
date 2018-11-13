try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import os.path
import re
import time
import random

class OCRRead:

    _ocr_file_type = ".txt"

    #This is just to make sure the user (hopefully) doesn't see the text that tells which iteration is which
    _text_separator = "text_separator"+hex(hash(random.random()))
    
    _current_iteration = 0
    

    def __init__(self, title, ocr_file_path=None, image_file_path=None, image_type=None):
        self.title = title

        if ocr_file_path is None:
            ocr_file_path = "./screen_text/"
        self.ocr_file_path = ocr_file_path

        if image_file_path is None:
            image_file_path = "./screen_shots/"
        self.image_file_path = image_file_path

        if image_type is None:
            image_type = ".png"
        self.image_type = image_type


    def ocr_read(self):
        print(self._current_iteration)

        # writes text from screen shot to this file
        screen_text_write = open(self.ocr_file_path + self.title + self._ocr_file_type, "a+")

        #goes through the screenshots being taken
        if os.path.exists(self.image_file_path + self.title + "_"+"%d" % self._current_iteration + self.image_type):
    
            start_time = time.time()
    
            #just formatting based on if it is the first (0th) self._current_iteration or not.
            # Don't need the \n\n, since no text is above
            if self._current_iteration == 0:
                #This is just used as an easier way to parse data, based on interations
                full_string = self._text_separator + " %d" % self._current_iteration + "\n"

            else:
                #This is just used as an easier way to parse data, based on interations
                full_string = "\n\n" + self._text_separator + " %d" % self._current_iteration + "\n"
    
            #convert image to text
            ocr_text = pytesseract.image_to_string(Image.open(self.image_file_path + self.title + "_"+"%d" % self._current_iteration
                                                              + self.image_type))
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
    
        screen_text_write.close()

        self._current_iteration += 1


    def get_text_separator(self):
        return self._text_separator
