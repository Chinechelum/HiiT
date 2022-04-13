import tkinter as tk
from tkinter import END

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

def clear_all():
    entry.delete(0, END)
# a = lambda x : entry.insert(0, x)

def delete():
    a = entry.get()
    entry.delete(len(a) - 1, END)

tk.Button(text = "1", command = lambda:click("1")).grid(row = "2", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "2", command = lambda:click("2")).grid(row = "2", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "3", command = lambda:click("3")).grid(row = "2", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "+", command = lambda:click("+")).grid(row = "2", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "4", command = lambda:click("4")).grid(row = "3", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "5", command = lambda:click("5")).grid(row = "3", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "6", command = lambda:click("6")).grid(row = "3", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "-", command = lambda:click("-")).grid(row = "3", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "7", command = lambda:click("7")).grid(row = "4", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "8", command = lambda:click("8")).grid(row = "4", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "9", command = lambda:click("9")).grid(row = "4", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "x", command = lambda:click("*")).grid(row = "4", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "0", command = lambda:click("0")).grid(row = "5", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = ".", command = lambda:click(".")).grid(row = "5", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "x\u00b2", command = lambda:click("**2")).grid(row = "5", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "/", command = lambda:click("/")).grid(row = "5", column = "3", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "del", command = delete).grid(row = "6", column = "0", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "C", command = clear_all).grid(row = "6", column = "1", ipadx = 3, ipady = 3, padx = 3, pady = 3)

tk.Button(text = "=", command = lambda: calculate("<Button-1>")).grid(row = "6", column = "2", ipadx = 3, ipady = 3, padx = 3, pady = 3)
# equals_btn.focus()




window.bind("<Return>", calculate)

window.mainloop()