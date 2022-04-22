import tkinter as tk
from tkinter import END
import winsound

window = tk.Tk()
window.title("My Calculator")
window.geometry("140x230")
window.resizable(False, False)


entry = tk.Entry()
entry.grid(row = "0", column = "0", columnspan = "4")
entry.focus()

def click(text):
    entry.insert('end', text)

def calculate(event):
    answer = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, answer)

def square_click(event):
    number = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"pow({number}, 2)")

def square_root_click(event):
    number = entry.get()
    entry.delete(0, END)
    entry.insert(0, f"pow({number}, 0.5)")

def clear_all():
    entry.delete(0, END)
# a = lambda x : entry.insert(0, x)

def delete():
    a = entry.get()
    entry.delete(len(a) - 1, END)

def sound(event):
    winsound.Beep(2300,40)

btn1 = tk.Button(text = "1", command = lambda:click("1"))
btn1.grid(row = "2", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn1.bind("<Button-1>", sound)

btn2 = tk.Button(text = "2", command = lambda:click("2"))
btn2.grid(row = "2", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn2.bind("<Button-1>", sound)

btn3 = tk.Button(text = "3", command = lambda:click("3"))
btn3.grid(row = "2", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn3.bind("<Button-1>", sound)

plus_btn = tk.Button(text = "+", command = lambda:click("+"))
plus_btn.grid(row = "2", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)
plus_btn.bind("<Button-1>", sound)

btn4 = tk.Button(text = "4", command = lambda:click("4"))
btn4.grid(row = "3", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn4.bind("<Button-1>", sound)

btn5 = tk.Button(text = "5", command = lambda:click("5"))
btn5.grid(row = "3", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn5.bind("<Button-1>", sound)

btn6 = tk.Button(text = "6", command = lambda:click("6"))
btn6.grid(row = "3", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn6.bind("<Button-1>", sound)

minus_btn = tk.Button(text = "-", command = lambda:click("-"))
minus_btn.grid(row = "3", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)
minus_btn.bind("<Button-1>", sound)

btn7 = tk.Button(text = "7", command = lambda:click("7"))
btn7.grid(row = "4", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn7.bind("<Button-1>", sound)

btn8 = tk.Button(text = "8", command = lambda:click("8"))
btn8.grid(row = "4", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn8.bind("<Button-1>", sound)

btn9 = tk.Button(text = "9", command = lambda:click("9"))
btn9.grid(row = "4", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn9.bind("<Button-1>", sound)

times_btn = tk.Button(text = "x", command = lambda:click("*"))
times_btn.grid(row = "4", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)
times_btn.bind("<Button-1>", sound)

btn0 = tk.Button(text = "0", command = lambda:click("0"))
btn0.grid(row = "5", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)
btn0.bind("<Button-1>", sound)

point_btn = tk.Button(text = ".", command = lambda:click("."))
point_btn.grid(row = "5", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)
point_btn.bind("<Button-1>", sound)

square_btn = tk.Button(text = "x\u00b2", command = lambda: square_click("<Button-1>"))
square_btn.grid(row = "5", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
square_btn.bind("<Button-1>", sound)

div_btn = tk.Button(text = "/", command = lambda:click("/"))
div_btn.grid(row = "5", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)
div_btn.bind("<Button-1>", sound)

del_btn = tk.Button(text = "del", command = delete)
del_btn.grid(row = "6", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)
del_btn.bind("<Button-1>", sound)

clear_btn = tk.Button(text = "C", command = clear_all)
clear_btn.grid(row = "6", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)
clear_btn.bind("<Button-1>", sound)

square_root_btn = tk.Button(text = "\u221ax", command = lambda: square_root_click("<Button-1>"))
square_root_btn.grid(row = "6", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
square_root_btn.bind("<Button-1>", sound)

equals_btn = tk.Button(text = "=", command = lambda: calculate("<Button-1>"))
equals_btn.grid(row = "6", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)
equals_btn.bind("<Button-1>", sound)

# equals_btn.focus()

window.bind("<Return>", calculate)

window.mainloop()
