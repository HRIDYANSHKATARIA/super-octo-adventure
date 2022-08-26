from tkinter import *
from PIL import ImageTk,Image
import os

root = Tk()
root.title("File Handling")
root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))
exit_image = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_filename = Label(root,text="File Name")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename = Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

open_button = Button(root,image=open_image,text="Open File")
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)



root.mainloop()