from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
from math import floor
import webbrowser


root = Tk()
root.title("Steganography")
root.resizable(0, 0)
root.configure(bg="white")

s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
window_width = 870
window_height = 510
x = int(int(s_width/2) - int(window_width/2))
y = int(int(s_height/2) - int(window_height/2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


filename = ""
flag = False


def open_image():
    global filename, flag
    text1["fg"] = "black"
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(), title="Choose File",
        filetypes=(("Aadil Says PNG file", "*.png"),
                   ("Aadil Says JPG file", "*.jpg"),
                   ("Aadil Says All file", "*.txt"))
    )
    try:
        img = Image.open(filename)
        basewidth = 275
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        resized_img = img.resize((basewidth, hsize))
        flag = True
    except:
        text1.delete(1.0, END)
        text1.insert(1.0, "Choose  an image file first".upper())
        text1["fg"] = "red"
        return
    img = ImageTk.PhotoImage(resized_img)
    display_image.configure(image=img)
    display_image.image = img
    text1.delete(1.0, END)


def save_secret():
    global filename, flag
    msg = str(text1.get(1.0, END))
    if (flag == False):
        text1.delete(1.0, END)
        text1.insert(1.0, "Choose  an image file first".upper())
    elif (len(str(msg)) == 1):
        text1.delete(1.0, END)
        text1.insert(1.0, "Enter Secret Text First".upper())
    else:
        secret = lsb.hide(str(filename), msg)
        secret.save(f"./Secret-Img.png")


def clear_data():
    try:
        secret = lsb.hide(str(filename), " ")
        secret.save(f"./Secret-Img.png")
        text1.delete(1.0, END)
    except:
        text1.delete(1.0, END)
        text1.insert(1.0, "There is no secret to clear".upper())


def show_data():
    msg = lsb.reveal(filename)
    if (msg):
        if (msg == " "):
            text1.delete(1.0, END)
            text1.insert(1.0, "There is no secret to show".upper())
        else:
            text1.delete(1.0, END)
            text1.insert(END, msg)
    else:
        text1.delete(1.0, END)
        text1.insert(1.0, "There is no secret".upper())


def clear_text():
    text1.delete(1.0, END)


# logo and images
logo = PhotoImage(file="./img/logo.png")
root.iconphoto(False, logo)
logo1 = PhotoImage(file="./img/logo1.png")
imgg = PhotoImage(file="./img/imgg.png")


Label(root, image=logo1, highlightthickness=0, bd=0).place(x=32, y=15)

Label(root, bg="white", fg="#444444", text="Hide Your Secret Text Inside An Image".upper(),
      font="arial 25 bold").place(x=80, y=11)

f1 = Frame(root, bd=2, bg="white", width=300, height=300, relief=GROOVE)
f1.place(x=45, y=90)

display_image = Label(f1, background="white",
                      fg="white", image=imgg)
display_image.place(x=10, y=14, width=275, height=272)

Lb1 = Label(root, text=" Picture File ", background="#444444", fg="white")
Lb1.place(x=45+10, y=80)

f2 = Frame(root, bd=2, bg="white", width=450, height=300, relief=GROOVE)
f2.place(x=45+330, y=90)
Lb2 = Label(root, text=" Hidden Text ", background="#444444", fg="white")
Lb2.place(x=45+330+10, y=80)

text1 = Text(f2, font="Robote 14", wrap=WORD,
             bg="white", bd=0, highlightthickness=0)
text1.place(x=10, y=10, width=408, height=270)
Scrollbar1 = Scrollbar(f2)
Scrollbar1.place(x=422, y=14, height=268)
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)


f3 = Frame(root, bd=0, highlightthickness=0, bg="white",
           width=300, height=50, relief=GROOVE)
f3.place(x=45, y=90+320)

f4 = Frame(root, bd=0, highlightthickness=0, bg="white",
           width=450, height=50, relief=GROOVE)
f4.place(x=45+330, y=90+320)

Button(f3, text="Open  Image".upper(), width=10, bd=2, highlightthickness=1, bg="white", command=open_image,
       height=2, relief=FLAT).place(x=0, y=0)
Button(f3, text="Make secret".upper(), width=10, bd=2, highlightthickness=1, bg="white", command=save_secret,
       height=2, relief=FLAT).place(x=120, y=0)

Button(f4, text="Clear  Secret".upper(), width=10, bd=2, highlightthickness=1, bg="white", command=clear_data,
       height=2, relief=FLAT).place(x=0, y=0)
Button(f4, text="Show  Data".upper(), width=10, bd=2, highlightthickness=1, bg="white", command=show_data,
       height=2, relief=FLAT).place(x=120, y=0)


Label(root, text="  Created By Aadil Mugal  ".upper(),
      background="#888888", fg="white").place(x=45, y=475)


github = PhotoImage(file="./img/github.png")
github_url = "https://github.com/aadilmughal786"
btn_github = Button(root, image=github, width=30-2, height=30, bd=0, bg="#ffffff", activebackground='#ffffff',
                    command=lambda: webbrowser.open(github_url), highlightthickness=0, highlightbackground="#ffffff")
btn_github.place(
    x=790, y=415)

dbin = PhotoImage(file="./img/bin.png")
btn_dbin = Button(root, image=dbin, width=30-2, height=30, bd=0, bg="#ffffff", activebackground='#ffffff',
                  command=clear_text, highlightthickness=0, highlightbackground="#ffffff")
btn_dbin.place(
    x=600, y=420)
root.mainloop()
