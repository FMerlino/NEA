#using tkinter create a calculator
import tkinter as tk
#from tkinter import *

root = tk.Tk()


#setting title
root.title('Calculator')

#size of the calculator
root.minsize(300, 400)
root.maxsize(300, 400)

#developing buttons
button_9 = tk.Button(root, text = '9').grid(row=2,column=3)
button_8 = tk.Button(root, text = '8').grid(row=2,column=2)
button_7 = tk.Button(root, text = '7').grid(row=2,column=1)
button_6 = tk.Button(root, text = '6').grid(row=3,column=3)
button_5 = tk.Button(root, text = '5').grid(row=3,column=2)
button_4 = tk.Button(root, text = '4').grid(row=3,column=1)
button_3 = tk.Button(root, text = '3').grid(row=4,column=3)
button_2 = tk.Button(root, text = '2').grid(row=4,column=2)
button_1 = tk.Button(root, text = '1').grid(row=4,column=1)
button_equal = tk.Button(root, text = '=').grid(row=5,column=3)
button_dot = tk.Button(root, text = '.').grid(row=5,column=2)
button_0 = tk.Button(root, text = '0').grid(row=5,column=1)

root.mainloop()