import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
import time
from tkinter import messagebox
#==============================================================================
################ Made by Steven (https://github.com/hi-ster)###################
#==============================================================================

#Window
root = tk.Tk()
root.title("Rock, Paper, Scissors - Tkinter")
canvas = tk.Canvas(root, width=600, height=450)
canvas.grid (columnspan=5, rowspan=7)
root.resizable(False, False)

#Image Boxes
#Player
pimg = Image.open('pplaceholder.png')
pimg = ImageTk.PhotoImage(pimg)
pimg_label = tk.Label(image=pimg)
pimg_label.image = pimg
pimg_label.grid(column=0, row=2)
#CPU
cimg = Image.open('cplaceholder.png')
cimg = ImageTk.PhotoImage(cimg)
cimg_label = tk.Label(image=cimg)
cimg_label.image = cimg
cimg_label.grid(column=3, row=2)

#Widgets
#player label
plabel = tk.Label(root, text="Player")
plabel.grid(column=0,row=0)
clabel = tk.Label(root, text="CPU")
clabel.grid(column=3, row=0)
#Made By
madebylabel = tk.Label(root, text="Made By Steven")
madebylabel.grid(column=0, row=6)

#Buttons - deal with spacing and aesthetics later
rockbtn = tk.Button(root, text="Rock", command=lambda:rockclicked(), height=2, width=6)
rockbtn.grid(column=0, row = 5)
sbtn = tk.Button(root, text="Scissors", command=lambda:scissorsclicked(), height=2, width=6)
sbtn.grid(column=1, row = 5)
pbtn = tk.Button(root, text="Paper", command=lambda:paperclicked(), height=2, width=6)
pbtn.grid(column=2, row = 5)
resetbtn = tk.Button(root, text="Reset", command=lambda:reset(), height=2, width=6)
resetbtn.grid(column=2, row =6)
#==============================================================================
rock ="rock"
paper = "paper"
scissors = "scissors"
cpu = ["rock", "paper", "scissors" ]
cpu_input = random.choice(cpu)

#CPU Pic Updates
def cpurock():
    cimg = Image.open('rock.png')
    cimg = ImageTk.PhotoImage(cimg)
    cimg_label = tk.Label(image=cimg)
    cimg_label.image = cimg
    cimg_label.grid(column=3, row=2)
def cpupaper():
    cimg = Image.open('paper.png')
    cimg = ImageTk.PhotoImage(cimg)
    cimg_label = tk.Label(image=cimg)
    cimg_label.image = cimg
    cimg_label.grid(column=3, row=2)
def cpuscissors():   
    cimg = Image.open('scissors.png')
    cimg = ImageTk.PhotoImage(cimg)
    cimg_label = tk.Label(image=cimg)
    cimg_label.image = cimg
    cimg_label.grid(column=3, row=2)
#Game Logic
def rockclicked():
    pimg = Image.open('rock.png')
    pimg = ImageTk.PhotoImage(pimg)
    pimg_label = tk.Label(image=pimg)
    pimg_label.image = pimg
    pimg_label.grid(column=0, row=2)
    time.sleep(1)
    cpu_input    
    if cpu_input == "rock":
        cpurock()
        messagebox.showinfo("Result", "Its a Draw.")
    elif cpu_input == "paper":
        cpupaper()
        messagebox.showinfo("Result","You Lose.")
    elif cpu_input == "scissors":
        cpuscissors()
        messagebox.showinfo("Result","You Win.")
def paperclicked():
    pimg = Image.open('paper.png')
    pimg = ImageTk.PhotoImage(pimg)
    pimg_label = tk.Label(image=pimg)
    pimg_label.image = pimg
    pimg_label.grid(column=0, row=2)
    time.sleep(1)
    cpu_input    
    if cpu_input == "rock":
        cpurock()
        messagebox.showinfo("Result","You Win.")
    elif cpu_input == "paper":
        cpupaper()
        messagebox.showinfo("Result", "Its a Draw.")
    elif cpu_input == "scissors":
        cpuscissors()
        messagebox.showinfo("Result","You Lose.")
def scissorsclicked():
    pimg = Image.open('paper.png')
    pimg = ImageTk.PhotoImage(pimg)
    pimg_label = tk.Label(image=pimg)
    pimg_label.image = pimg
    pimg_label.grid(column=0, row=2)
    time.sleep(1)
    cpu_input    
    if cpu_input == "rock":
        cpurock()
        messagebox.showinfo("Result","You Lose.")
    elif cpu_input == "paper":
        cpupaper()        
        messagebox.showinfo("Result","You Win.")
    elif cpu_input == "scissors":
        cpuscissors()
        messagebox.showinfo("Result", "Its a Draw.")
def reset():
    #Player
    pimg = Image.open('pplaceholder.png')
    pimg = ImageTk.PhotoImage(pimg)
    pimg_label = tk.Label(image=pimg)
    pimg_label.image = pimg
    pimg_label.grid(column=0, row=2)
    #CPU
    cimg = Image.open('cplaceholder.png')
    cimg = ImageTk.PhotoImage(cimg)
    cimg_label = tk.Label(image=cimg)
    cimg_label.image = cimg
    cimg_label.grid(column=3, row=2)
    


root.mainloop()
