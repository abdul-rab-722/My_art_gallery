import tkinter as tk
from tkinter import filedialog
from tkinter import *
from style_transfer import transfer_style
from PIL import ImageTk, Image
import cv2
import os

top=tk.Tk()
top.geometry('1000x600')
top.title('My Art Gallery')
top.iconbitmap('.\\images\\icons\\mag_icon.ico')
top.configure(background='white')
    
def convert(file_path,fil,new):
    styled_img=transfer_style(file_path,fil)
    cv2.imshow('new',styled_img)

def pick_filter(file_path,new):
    filter_text=Label(new,text='Pick a filter to apply')
    filter_text.configure(background='white', foreground='#05232c', font='arial 14 bold underline')
    filter_text.place(x=30,y=30)
    filters=os.listdir('.\\images\\filters')
    i=10
    for fil in range(len(filters)):
        im=Image.open(f'.\\images\\filters\\{filters[fil]}')
        im.thumbnail(((new.winfo_width()/8),(new.winfo_height()/8)))
        im=ImageTk.PhotoImage(im)
        label=Label(new,image=im,cursor="hand2")
        label.image=im
        label.place(x=i,y=480); i+=new.winfo_width()/9.31
        label.bind("<1>",lambda e,f=fil:convert(file_path,f'.\\images\\filters\\{filters[f]}',new))

def new_image(im,file_path):
    new=Toplevel()
    new.geometry('1000x600')
    new.title('New Project')
    new.iconbitmap('.\\images\\icons\\mag_icon.ico')
    new.configure(background='white')
    label=Label(new,image=im)
    label.image=im
    label.pack(side="left", expand='yes')
    pick_filter(file_path, new)

def upload_image():
    file_path=filedialog.askopenfilename()
    try:
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        new_image(im,file_path)
    except:
        pass

mag_img=Image.open('.\\images\\others\\My Art Gallery.jpg')
mag_img.thumbnail((top.winfo_width(),top.winfo_height()))
mag_img=ImageTk.PhotoImage(mag_img)
mag_label=Label(top,image=mag_img)
mag_label.image=mag_img
mag_label.pack(side='top',expand='yes')

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#05232c',foreground='white',font=('arial',10,'bold'))
upload.place(relx=0.44,rely=0.89)

top.mainloop()
