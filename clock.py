from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime("%H:%M:%S")
    lbl.config(text=string) 
    lbl.after(1000,time)
    
lbl=Label(root, font= ("times new roman", 40, "bold"),
          background="black", 
          foreground="white")

lbl.pack(anchor="center")

time()
mainloop()
