# import system functions
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

curl -L https://static.ironside.org.uk/cfgui/logo.png -o ~/cfgui/logo.png


# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='~/cfgui/logo.png'))

def connect():
    print("Please accept the terms and conditions shown below.")
    os.system("warp-cli register")
    print("Beginning connection")
    os.system("warp-cli connect")
    root.iconphoto(False, tk.PhotoImage(file='~/cfgui/logo.png'))
    messagebox.showinfo("Cloudflare WARP", "Connected successfully")
    
def disconnect():
    print("Stopping connection")
    os.system("warp-cli disconnect")
    root.iconphoto(False, tk.PhotoImage(file='~/cfgui/logo.png'))
    messagebox.showinfo("Cloudflare WARP", "Disconnected successfully")
    
def register():
    print("Please accept the terms and conditions shown below.")
    os.system("warp-cli register")
    root.iconphoto(False, tk.PhotoImage(file='~/cfgui/logo.png'))
    messagebox.showinfo("Cloudflare WARP", "Registered successfully")
   
root.title('Cloudflare WARP')
frame.pack()

#BIG title on program
mainText = Label(root, text="Cloudflare WARP",font=('Helveticabold', 24))
mainText.place(x=10, y=5)
#label

cButton1 = tk.Button(frame,
                   text="Connect",
                   command=connect,
                   state="normal")
cButton1.place(x=10, y=50)

cButton2 = tk.Button(frame,
                   text="Disconnect",
                   command=disconnect,
                   state="normal")
cButton2.place(x=10, y=80)

img2 = Image.open("~/cfgui/logo.png")
#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
NewIMGSize2 = img2.resize((100,100), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(NewIMGSize2)
label = Label(frame, image = new_image2)
label.place(x=390, y=0)

#Create a Label to display the link

root.geometry("500x250")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')

root.mainloop()
