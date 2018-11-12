try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import os.path
import re
import time

class OCRRead:

    _ocr_file_type = ".txt"


    #TODO: Need to make kwargs work so is more versatile
    #def __init__(self, **kwargs):

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


    def ocr_read(self, iteration):

        # writes text from screen shot to this file
        screen_text_write = open(self.ocr_file_path + self.title + self._ocr_file_type, "a+")

        #goes through the screenshots being taken
        if os.path.exists(self.image_file_path + self.title + "_"+"%d" % iteration + self.image_type):
    
            start_time = time.time()
    
            #just formatting based on if it is the first (0th) iteration or not.
            # Don't need the \n\n, since no text is above
            if iteration == 0:
                #This is just used as an easier way to parse data, based on interations
                full_string = "zzzzzzzzzzziteration: %d" % iteration + "\n"
            else:
                #This is just used as an easier way to parse data, based on interations
                full_string = "\n\nzzzzzzzzzzziteration: %d" % iteration + "\n"
    
            #convert image to text
            ocr_text = pytesseract.image_to_string(Image.open(self.image_file_path + self.title + "_"+"%d" % iteration
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
