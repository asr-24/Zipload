import os
import shutil


def zipdir (path, final):
    shutil.make_archive(final,"zip",path)
    

zipdir("C:\\Users\\10aru\\Documents\\work22\\python\\Ex_Files_Building_Tools_Python\\Exercise Files\\decks", "C:\\Users\\10aru\\Documents\\work22\\python\\Zipload\\individual_functions\\finalZIP")

