from tkinter import *
import os
import tkinter.scrolledtext as st
from tkinter import filedialog


def of():
    f2 = filedialog.askopenfile(mode='rb', title='Select a File', filetypes=(('Text File', '*.txt'), ('All', '*.*')))
    if f2 != None:
        contold = f2.read()
        cont.insert('1.0', contold)
        f2.close()


def sf():
    f3 = filedialog.asksaveasfile(mode='w', title='Save File')
    if f3 != None:
        contnew = cont.get('1.0', END + '-1c')
        f3.write(contnew)
        f3.close()


def nf():
    cont = st.ScrolledText(w4, width=700, height=500)
    cont.pack()


def diary():
    global w4
    w4 = Tk()
    w4.title('Diary')
    w4.geometry("800x600")
    w3.destroy()

    global cont
    cont = st.ScrolledText(w4, width=700, height=500)
    cont.pack()

    m = Menu(w4)
    w4.config(menu=m)

    m1 = Menu(m)
    m.add_cascade(label='File', menu=m1)
    m1.add_command(label='New', command=nf)
    m1.add_command(label='Open', command=of)
    m1.add_command(label='Save', command=sf)
    m1.add_separator()
    m1.add_command(label='Exit', command=exit)

    m2 = Menu(m)
    m.add_cascade(label='Edit', menu=m2)
    m2.add_command(label='Templates', command=nf)
    m2.add_command(label='Fonts', command=nf)
    m2.add_command(label='Color', command=nf)


def home():
    global w3
    w3 = Tk()
    w3.title('Home')
    w3.geometry("800x600")
    w2.destroy()

    h31 = Label(w3, text='Home', bg='purple', height=3)
    h31.pack(fill=X)

    s31 = Label(w3, text='', height=3)
    s31.pack()

    b31 = Button(w3, text='Diary', bg='green', width=30, height=2, command=diary)
    b31.pack()

    s32 = Label(w3, text='', height=1)
    s32.pack()

    b32 = Button(w3, text='Log Out', bg='green', width=30, height=2, command=exit)
    b32.pack()


def sav():
    nam = e11.get()
    pas = e12.get()
    f1 = open(nam, 'w')
    f1.write(nam + '\n')
    f1.write(pas)
    f1.close()

    e11.delete(0, END)
    e12.delete(0, END)

    h111 = Label(w1, text='Saved!', fg='blue', width=20, height=2)
    h111.pack()

    w1.destroy()


def reg():
    global w1
    # w1 = Toplevel(w)
    w1 = Tk()
    w1.title('Register')
    w1.geometry("300x350")

    global e11
    global e12

    h10 = Label(w1, text='Enter Your Details:', bg='purple', height=3)
    h10.pack(fill=X)

    s11 = Label(w1, text='', height=2)
    s11.pack()

    h11 = Label(w1, text='Name:', bg='green', width=20, height=2)
    h11.pack()

    e11 = Entry(w1)
    e11.pack()

    s12 = Label(w1, text='', height=1)
    s12.pack()

    h12 = Label(w1, text='Password:', bg='green', width=20, height=2)
    h12.pack()

    e12 = Entry(w1)
    e12.pack()

    s13 = Label(w1, text='', height=1)
    s13.pack()

    b11 = Button(w1, text='Save', bg='orange', width=20, height=2, command=sav)
    b11.pack()


def ret():
    vnam = e21.get()
    vpas = e22.get()

    e21.delete(0, END)
    e22.delete(0, END)

    lof = os.listdir()
    if vnam in lof:
        f2 = open(vnam , 'r')
        nl = f2.read().splitlines()
        if vpas in nl:
            h211 = Label(w2, text='Logged In Successfully!', fg='blue', width=20, height=2)
            h211.pack()
            home()
        else:
            print('Wrong Password!')
    else:
        print('Invalid Username')




def log():
    global w2
    w2 = Tk()
    w2.title('Login')
    w2.geometry("300x350")

    global e21
    global e22

    h20 = Label(w2, text='Enter Your Credentials:', bg='purple', height=3)
    h20.pack(fill=X)

    w.destroy()

    s21 = Label(w2, text='', height=2)
    s21.pack()

    h21 = Label(w2, text='Name:', bg='green', width=20, height=2)
    h21.pack()

    e21 = Entry(w2)
    e21.pack()

    s22 = Label(w2, text='', height=1)
    s22.pack()

    h22 = Label(w2, text='Password:', bg='green', width=20, height=2)
    h22.pack()

    e22 = Entry(w2)
    e22.pack()

    s23 = Label(w2, text='', height=1)
    s23.pack()

    b21 = Button(w2, text='Sign In', bg='orange', width=20, height=2, command=ret)
    b21.pack()


global w
w = Tk()
w.title('Main')
w.geometry("300x250")

h1 = Label(w, text='Morning!', bg='purple', height=3)
h1.pack(fill=X)

s1 = Label(w, text='', height=3)
s1.pack()

b1 = Button(w, text='Login', bg='green', width=30, height=2, command=log)
b1.pack()

s2 = Label(w, text='', height=1)
s2.pack()

b2 = Button(w, text='Register', bg='green', width=30, height=2, command=reg)
b2.pack()


w.mainloop()
