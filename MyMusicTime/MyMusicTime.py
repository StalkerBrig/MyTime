from scipy import misc
import Image
import numpy as np
import sys
import os

screen_name = sys.argv[1] + "_"
screen_type = ".png"

iteration = 0

screen_full_file_name = screen_name + str(iteration) + screen_type
screen_path = "../screen_shots/" + screen_full_file_name

screen_average_color_path = "./screen_average_color/"



while os.path.exists(screen_path):

    im = Image.open(screen_path)

    pixels = list(im.getdata())

    avg_pixel = [0, 0, 0]

    width, height = im.size

    for pixel in pixels:
        avg_pixel += np.array(pixel)

    avg_pixel = avg_pixel/(width*height)

    avg_pixel = tuple(avg_pixel)
    average_image = Image.new('RGB', (1, 1), color = avg_pixel)

    average_color_file_name = screen_name + "avg_" + str(iteration) + screen_type

    average_image.save(screen_average_color_path+average_color_file_name)

    iteration += 1

    screen_full_file_name = screen_name + str(iteration) + screen_type
    screen_path = "../screen_shots/" + screen_full_file_name
