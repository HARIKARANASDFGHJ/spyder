# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:20:22 2023

@author: Admin
"""
#0
from tkinter import *


root = Tk() 

root.mainloop() 

#1

from tkinter import *

main_window = Tk()
# Labels

Label (main_window, text= "Hello World").pack()

Label (main_window, text="This is Tkinter").pack()

main_window.mainloop()

#2

from tkinter import *

main_window = Tk()

# Labels

Label (main_window, text= "Hello World").grid(row= 0, column = 0)

Label (main_window, text="This is Tkinter").grid(row = 0, column=1)

main_window.mainloop()


#3

from tkinter import *

main_window = Tk()

# Labels

Label (main_window, text= "Hello World").grid(row= 0, column = 0)

Label (main_window, text="This is Tkinter").grid(row = 1, column =0)

Entry(main_window, width=50, borderwidth = 5).grid(row = 0, column = 1)

Entry(main_window, width=50, borderwidth = 5).grid(row = 1, column = 1)

main_window.mainloop()

#4

from tkinter import *

main_window = Tk()

# Labels

Label(main_window, text="Enter your name").grid(row= 0, column = 0)

Label(main_window, text="Enter your age").grid(row = 1, column =0)

my_name=Entry(main_window, width=50, borderwidth = 5)
my_name.grid(row = 0, column = 1)

my_age=Entry(main_window, width=50, borderwidth = 5)
my_age.grid(row = 1, column = 1)



def on_click():
    
    print(f"my name is {my_name.get()}, my age is {my_age.get()}")
    

#Buttons

Button (main_window, text="Click Me", command = on_click).grid(row=2, column=1)

main_window.mainloop()



















