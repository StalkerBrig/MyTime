import pyscreenshot as ImageGrab
from screeninfo import get_monitors
import time
import sys
from PIL import ImageFilter
from PIL import Image

class ScreenCapture:
    
    _current_iteration = 0

    def __init__(self, title, my_music_time_title=None, my_music_time=None, file_path=None, image_type=None):

        self.title = title

        if my_music_time_title is None:
            my_music_time_title = "color"
        self.my_music_time_title = my_music_time_title

        if my_music_time is None:
            my_music_time = False
        self.my_music_time = my_music_time

        if file_path is None:
            file_path = "./screen_shots/"
        self.file_path = file_path

        if image_type is None:
            image_type = ".png"
        self.image_type = image_type

        #_screen_height and _screen_width defined here
        self._monitor_size()

    # Gets the size of the user's monitor
    def _monitor_size(self):
        get_monitors_str = str(get_monitors())

        _screen_width_str = ""
        _screen_height_str = ""

        # Parses the string with the monitor size; will get the width and height
        for letter_index in range(len(get_monitors_str)):

            # a '(' is the character right before the width
            if get_monitors_str[letter_index] == "(":
                # need to increase by 1 so it doesn't copy the '('
                letter_index += 1
                # 'x' is the character after the last number in the width
                while (get_monitors_str[letter_index] != "x"):
                    # copys all numbers for width
                    _screen_width_str += get_monitors_str[letter_index]
                    letter_index += 1

                # the character past the 'x' starts the heigth, so need to increase by 1
                letter_index += 1

                # the character past the height is '+', so loop until we hit the '+'
                while (get_monitors_str[letter_index] != "+"):
                    # copys all numbers for height
                    _screen_height_str += get_monitors_str[letter_index]
                    letter_index += 1

                # don't need anything else after this, so can break out loop
                break

        self._screen_width = int(_screen_width_str)
        self._screen_height = int(_screen_height_str)

    def take_screen_shot(self):
        #gets a screenshot of user screen
        screen_shot_color = ImageGrab.grab(bbox=(0, 0, self._screen_width, self._screen_height))

        #Making the image bigger; helps the OCR read it
        screen_shot_color = screen_shot_color.resize((self._screen_width*2, self._screen_height*2), Image.NEAREST)
        screen_shot_color.filter(ImageFilter.SHARPEN)

        #Converts to black white; easier for OCR readers
        screen_shot_bw = screen_shot_color.convert('L')

        #saves screen shot to a file
        screen_shot_bw.save(self.file_path + self.title + "_" + str(self._current_iteration) + self.image_type, quality=300)

        #saves color screen shot for MyMusicTime
        if self.my_music_time == True:
            screen_shot_color.save(self.file_path + self.title + "_" + self.my_music_time_title + "_"
                                   + str(self._current_iteration) + self.image_type, quality=300)

        self._current_iteration += 1
