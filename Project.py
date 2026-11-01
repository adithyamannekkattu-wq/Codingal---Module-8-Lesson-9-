from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root=Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x450")

title=Label(root, text="Rock, Paper, Scissiors", fg="black", bg="lightyellow")
title.pack(anchor="center", pady=10)

player=Label(root, text="Enter your choice: ", fg="black")
player.pack(anchor="w", pady=5, padx=10)

player_entry=Entry(root, width=30, fg="black", bg="lightyellow")
player_entry.pack(anchor="w", pady=5, padx=10)


def sub():
    computer=random.choice(["rock", "paper", "scissors"])
    guess=player_entry.get()

    top=Toplevel()
    top.geometry("400x350")
    top.title("result")

    if guess==computer:
        compute=Label(top, text="Computer Choice: ", fg="black")
        compute.pack(pady=5, anchor="w", padx=10)
        cmpute=Label(top, text=computer, fg="black")
        cmpute.pack(pady=5, anchor="w", padx=10)

        result=Label(top, text="You won!", fg="black")
        result.pack(pady=5)


    else:
        compute=Label(top, text="Computer Choice: ", fg="black")
        compute.pack(pady=5, anchor="w", padx=10)
        cmpute=Label(top, text=computer, fg="black")
        cmpute.pack(pady=5, anchor="w", padx=10)

        result=Label(top, text="You lost!", fg="black")
        result.pack(pady=5)

    top.mainloop()

submit=Button(root, text="Submit", fg="white", bg="red", command=sub)
submit.pack(pady=5)
        

root.mainloop()