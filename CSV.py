
#This Python file is to handle

from csv import reader
from os import walk

from PIL import Image, ImageTk


def csv_layout(path):
    map = []
    with open(path) as level_map:
        layout = reader (level_map, delimiter = ',')
        for row in layout:
            map.append(list(row))
        return map

# To pull all the photos out of a folder and put into a list
def import_folder(path, size):
    surface_list = []
    for __,__,img_files  in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_PIL = Image.open(full_path).resize((size[0], size[1]))
            tkinterImage = ImageTk.PhotoImage(image_PIL)

            surface_list.append(tkinterImage)
        return surface_list



