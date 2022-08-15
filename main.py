from tkinter import *
import os
from tkinter import messagebox
tk = Tk()
tk.geometry("350x400")
tk.config(bg="grey")
tk.title("Python Login And Register System By VirusNoir")
Label(tk,text="A Simple Login & Register System Using Python Tkinter \n Follow Me On Github : @VirusNoirrr \n And Instagram : @not_elli0t",bg="grey",fg="blue",justify="left",font=("Timer",10)).place(x=3)
user_lbl = Label(tk,text="Username : ",bg="grey",fg="black",font=("Times",18))
user_lbl.pack()
user_lbl.place(x=15,y=150)
password_lbl = Label(tk,text="Password : ",bg="grey",fg="black",font=("Times",18))
password_lbl.pack()
password_lbl.place(x=15,y=200)

user_entry = Entry(tk,border=5)
user_entry.pack()
user_entry.place(x=150,y=157)

password_entry = Entry(tk,border=5)
password_entry.pack()
password_entry.place(x=150,y=205)
def login():
    if os.path.exists(f"{user_entry.get()}.txt"):
        usr_file = open(f"{user_entry.get()}.txt").read()
        usr = usr_file.split('\n',1)[0]
        pass_file = open(f"{user_entry.get()}.txt").read()
        password = pass_file.split('\n',1)[1]
        if user_entry.get() == usr:
            if password_entry.get() == password:
                messagebox.showinfo("Login Info",f"You Are Loggined In As {usr}")
            else:
                messagebox.showerror("Login Error","Password Incorrect !")
    else:
        messagebox.showerror("Login Error","I Cant Found This Username In My Database !!")
        


submit = Button(tk,text="Submit",bg="black",fg="white",command=login,font=("Timer",18))
submit.pack()
submit.place(x=15,y=250)
def register():
    reg = Tk()
    reg.geometry("350x400")
    reg.config(bg="grey")
    reg.title("Register")
    username = Label(reg,text="Register Username : ", bg="grey",fg="black",font=("Times", 18))
    username.pack()
    username.place(x=15,y=150)
    password = Label(reg,text="Register Password : ",bg="grey",fg="black",font=("Times", 18))
    password.pack()
    password.place(x=15,y=200)

    username_entry = Entry(reg,border=5)
    username_entry.pack()
    username_entry.place(x=215,y=157)

    password_entry = Entry(reg,border=5)
    password_entry.pack()
    password_entry.place(x=210,y=205)
    def regi():
        with open(username_entry.get()+".txt","w") as f:
            f.write(username_entry.get() + '\n')
            f.write(password_entry.get())
    btn = Button(reg,text="Submit",bg="black",fg="white",command=regi,font=("Timer",18))
    btn.pack()
    btn.place(x=15,y=290)
    login = Button(reg, text="Login",bg="grey",fg="green",command=reg.destroy,font=("Timer",18))
    login.pack()
    login.place(x=15,y=350)


reg = Button(tk,text="Register",bg="grey",fg="green",command=register,font=("Timer",18))
reg.pack()
reg.place(x=15,y=290)
mainloop()