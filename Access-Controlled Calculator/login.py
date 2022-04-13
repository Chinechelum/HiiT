import tkinter as tk
import sqlite3
from tkinter import messagebox as mb

main_window = tk.Tk()
main_window.title("Login Page")
main_window.geometry("300x300")


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        mb.showerror(message="Username and Password must be inputted")
    else:
        with sqlite3.connect("usersdetails.db") as db:
            cursor = db.cursor()
            # cursor.execute("INSERT INTO userprofile VALUES ('john', 'john123')")
            rows = cursor.execute("SELECT username, password FROM userprofile").fetchall()

            if rows.__contains__((username, password)):
                mb.showinfo(message=f"{username}, welcome")
                main_window.destroy()
                import my_calculator
            else:
                mb.showerror(message="User not registered")

        
            rows = cursor.execute("SELECT username, password FROM userprofile").fetchall()
            print(rows)
    
def register():
    main_window.destroy()
    import register
            


label1 = tk.Label(text="username", bg="black", fg="white")
label1.grid(row=0, column=0)

label2 = tk.Label(text="password", bg="black", fg="white")
label2.grid(row=1, column=0)

username_entry = tk.Entry()
username_entry.grid(row=0, column=5, columnspan=3)

password_entry = tk.Entry(show="*")
password_entry.grid(row=1, column=5, columnspan=3)

login_button = tk.Button(text="Login", bg="yellow", command=login)
login_button.grid(row=2, column=2, columnspan=4)

register_button = tk.Button(text="Register instead", bg="yellow", command=register)
register_button.grid(row=4, column=2, columnspan=4)


# button2 = tk.Button(text="login", bg="yellow")
# button2.pack()




main_window.mainloop()