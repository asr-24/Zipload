from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

print(os.getcwd())

os.chdir("C:\\Users\\10aru\Documents\\work22\\python\\Zipload")

gauth = GoogleAuth()

drive = GoogleDrive(gauth)

uploadThis = "C:\\Users\\10aru\\Documents\\work22\\python\\Zipload\\individual_functions\\finalZIP.zip"

upload_file_list = [
   uploadThis
    ]


for upload_file in upload_file_list:
    gfile = drive.CreateFile(
        {'title': 'NewFile',
         'parents' : [{'id' : 
                       '1NalwOAc1uoW8-aIBSLPztGKS0M-sb9RN'
                       }]}
        )
    gfile.SetContentFile(upload_file)
    gfile.Upload()
