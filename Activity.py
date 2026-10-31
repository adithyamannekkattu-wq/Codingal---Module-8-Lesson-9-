from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title("Denomination Calculator")
root.geometry("500x475")

title=Label(root, text="Denomination Calculator", fg="blue", bg="lightyellow")
title.pack(pady=5)

image=Image.open("cal.jpg")
image=image.resize((300, 250))
photo=ImageTk.PhotoImage(image)
pic=Label(root, image=photo)
pic.pack(pady=5)

def box():
    messagebox.showinfo("Information", "You will be asked to input an amount and the program will find out whicj all notes you need")

show_box=Button(root, text="Show info", fg="white", bg="red", command=box)
show_box.pack(pady=5)

amount=None

def popup():
    top=Toplevel()
    top.title("Amount Printer")
    top.geometry("475x450")

    title=Label(top, text="Calculator", fg="red", bg="lightyellow")
    title.pack(pady=5)

    
    l1=Label(top, text="Amount: ", fg="black", bg="white")
    l1.pack(padx=5)
    e1=Entry(top, width=25, fg="black", bg="lightyellow")
    e1.pack(pady=5)

    def submit():
        try:
            amount=int(e1.get())
            label1=Label(top, text="2000 notes: ", fg="black", bg="white")
            label1.pack(pady=5)
            label4=Label(top, text=note2000, fg="black", bg="white")
            label4.pack(pady=5)
        
            label2=Label(top, text="500 notes: ", fg="black", bg="white")
            label2.pack(padx=5)
            label5=Label(top, text=note500, fg="black", bg="white")
            label5.pack(pady=5)
        
            label3=Label(top, text="100 notes: ", fg="black", bg="white")
            label3.pack(padx=5)
            label6=Label(top, text=note100, fg="black", bg="white")
            label6.pack(pady=5)
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note100=amount//100
            amount%=100
        except ValueError:
            print("Enter a valid value")

    sb=Button(top, text="submit", fg="black")
    sb.pack(pady=5)


    top.mainloop()

show_top=Button(root, text="Calculate", fg="white", bg="red", command=popup)
show_top.pack(pady=5)


root.mainloop()
