import os
import re
import zipfile
import tkinter
from tkinter import filedialog, messagebox
import customtkinter
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import shutil
import datetime


def show_error(text):
    tkinter.messagebox.showerror('Error', text)

def show_results(text):
    tkinter.messagebox.showinfo('Results', text)

def dateTimeTag():
    tag = str(datetime.datetime.now())
    tag = tag.replace("-","_")
    tag = tag.replace(" ","__")
    tag = tag.replace(":","")
    return tag[:tag.index('.')]


def zipIt(folder):
    folder_destination = "C:\\Users\\10aru\\Documents\\work22\\python\\Zipload\\ZippedFiles"
    date_time_tag = dateTimeTag()
    
    final_destination = folder_destination + "\\" + date_time_tag

    try:   
        shutil.make_archive(final_destination, "zip", folder)
        return (1, final_destination)
    except Exception as e:
        return (0, '')


def returnTag(folder, flag = 1):
    temp1 = folder[::-1]
    here = "/"
    if flag == 1:
        here = "\\"

    temp2 = temp1[:temp1.index(here)]
    temp3 = temp2[::-1]

    return temp3


    



def ziploadThese(folder):
    ret_from_zipit = zipIt(folder)
    print(folder)
    print(type(folder))

    folder_name = returnTag(folder, 0)

    results = 'Operation failed, please try again later!'

    if ret_from_zipit[0] == 0:
        show_error("Unable to ZIP folder at %s" %(folder))
    else:
        zipped_folder = ret_from_zipit[1]
        updated_title = returnTag(zipped_folder)

        try:
            gauth = GoogleAuth()
            drive = GoogleDrive(gauth)
            
            upload_this = zipped_folder + '.zip'

            gfile = drive.CreateFile(
                {'title': updated_title,
                 'parents' : [{'id' : 
                               '1NalwOAc1uoW8-aIBSLPztGKS0M-sb9RN'
                               }]}
                )
            gfile.SetContentFile(upload_this)
            gfile.Upload()

            results = "Folder uploaded successfully!"

        except Exception as e:
            show_error("Error uploading file, please try again later!")
            print(e)


    show_results(results)



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() 
app.geometry("400x240")
app.title("Zipload")

def clicked():
    folder = tkinter.filedialog.askdirectory()
    ziploadThese(folder)
    print(folder)

app.welcome_label= customtkinter.CTkLabel(text="          Welcome to Zipload",text_font=("Roboto Medium", -24))
app.welcome_label.grid(row=0, column=0, pady=20, padx=20, sticky="nwe")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text = "Choose the folder to be Ziploaded", command=clicked)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.welcome_label= customtkinter.CTkLabel(text="                      a python tool by arushi",text_font=("Roboto Medium", -12))
app.welcome_label.grid(row=10, pady=130, column=0, sticky="nwe")

app.mainloop()


"""
app = customtkinter.CTk() 
app.geometry("400x240")
app.title("Zipload")


def clicked():
    folder = tkinter.filedialog.askdirectory()
    ziploadThese(folder)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create the window header.

app.label_radio_group = customtkinter.CTkLabel(text="Welcome to Zipload!",text_font=("Roboto Medium", -24))
app.label_radio_group.grid(row=0, column=0, columnspan=5, pady=20, padx=10, sticky="")


#header = tkinter.Label(app, text="Welcome to Zipload!", fg="orange", font=("Arial Bold", 16))
#header.pack(side="top", ipady=10)

# Add the descriptive text.
#text = tkinter.Label(app, text="Select a folder, and the\n app will ZIP it and upload it to your Google Drive.")
#text.pack()


# Draw the button that opens the file picker.
open_files = tkinter.Button(app, text="Choose folder...", command=clicked)
open_files.config(height=50,
                  width=56)
#open_files.pack()

# Initialize Tk window.
app.mainloop()
"""