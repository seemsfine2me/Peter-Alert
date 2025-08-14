#imports tkinter
import tkinter as tk
from tkinter import *
import time 
import random
#imports pillow form the Python Image Libary or somthing 
from PIL import Image, ImageTk
#numeber lists
list = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2 = [1,2,3,4,5,6,7,9,10,11,12,13]
#rizz = True
rizz = True
#def ran
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
    
#def the tkinter stuff
def main():
    #bare bones stuff
    global root 
    root = tk.Tk()
    root.title('Peter Alert')
    root.geometry("730x400")
    global rizz
    rizz = False
    #gets the image and converts it

    image = Image.open("peter.png")
    tk_image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=tk_image)
    label.pack()
    #button
    button = Button(root, text = 'Peter Alert', command=root.destroy)  
    button.pack()
    root.mainloop()
    rizz = True

    
ran()
