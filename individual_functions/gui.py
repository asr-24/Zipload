import tkinter
import tkinter.filedialog
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() 
app.geometry("400x240")
app.title("Zipload")

def clicked():
    folder = tkinter.filedialog.askdirectory()
    #ziploadThese(folder)
    print(folder)

app.welcome_label= customtkinter.CTkLabel(text="          Welcome to Zipload",text_font=("Roboto Medium", -24))
app.welcome_label.grid(row=0, column=0, pady=20, padx=20, sticky="nwe")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text = "Choose the folder to be Ziploaded", command=clicked)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.welcome_label= customtkinter.CTkLabel(text="                      a python tool by arushi",text_font=("Roboto Medium", -12))
app.welcome_label.grid(row=10, pady=130, column=0, sticky="nwe")

app.mainloop()
