import tkinter as tk
import sqlite3
from tkinter import messagebox as mb

main_window = tk.Tk()
main_window.title("Register Page")
main_window.geometry("300x300")


def register():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        mb.showerror(message="Username and Password must be inputted")
    else:
        with sqlite3.connect("usersdetails.db") as db:
            cursor = db.cursor()
            # cursor.execute("INSERT INTO userprofile VALUES ('john', 'john123')")
            rows = cursor.execute("SELECT username, password FROM userprofile").fetchall()

            def matches(rows, username):
                for user in rows:
                    if user[0] == username:
                        return True

            if not matches(rows, username):
                cursor.execute("INSERT INTO userprofile(username,password) VALUES (?, ?)",(username, password))
                mb.showinfo(message="Welcome")
                main_window.destroy()
                import my_calculator
            else:
                mb.showinfo(message="Username already used. Try again.")

        
            rows = cursor.execute("SELECT username, password FROM userprofile").fetchall()
            print(rows)

def login():
    main_window.destroy()
    import login
    
            


label1 = tk.Label(text="username", bg="black", fg="white")
label1.grid(row=0, column=0)

label2 = tk.Label(text="password", bg="black", fg="white")
label2.grid(row=1, column=0)

username_entry = tk.Entry()
username_entry.grid(row=0, column=5, columnspan=3)

password_entry = tk.Entry(show="*")
password_entry.grid(row=1, column=5, columnspan=3)

register_button = tk.Button(text="Register", bg="yellow", command=register)
register_button.grid(row=2, column=2, columnspan=4)


login_button = tk.Button(text="Login instead", bg="yellow", command=login)
login_button.grid(row=4, column=2, columnspan=4)

# button2 = tk.Button(text="login", bg="yellow")
# button2.pack()




main_window.mainloop()