

from tkinter import *
import tkinter as tk
import webbrowser

def doorbell(event):
    print("you rang the doorbell")

def open_cp(event):
    webbrowser.open_new_tab('https://cleaverprogrammer.com')

window = tk.tk()
window.geometry("300x200")

button=tk.Button(window,text="Doorbell")
button.grid(coloumn=0)

button1=tk.Button(window,text="CleaverProgrammer")
button1=grid(coloumn=1,row=1)
button.bind("<Button-1>",doorbell)
button1.bind("<Button-1>",open_cp)
window.mainloop()
