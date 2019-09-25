#using tkinter create a calculator

import tkinter as tk
from tkinter import Button

root = tk.Tk()


#setting title
root.title('Calculator')

#size of the calculator
root.minsize(300, 400)
root.maxsize(300, 400)

#developing buttons
def buttons():
    Button(root, text = '6').pack(side = TOP)
    Button(root, text = '5').pack(side = TOP)
    Button(root, text = '4').pack(side = TOP)
    Button(root, text = '3').pack(side = TOP)
    Button(root, text = '2').pack(side = TOP)
    Button(root, text = '1').pack(side = TOP)
    Button(root, text = '=').pack(side = LEFT)
    Button(root, text = '.').pack(side = LEFT)
    Button(root, text = '0').pack(side = LEFT)


w.pack()
root.mainloop()