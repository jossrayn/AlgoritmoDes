from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import os.path

import ClaveDes

from Des2 import *

from Des3 import *

def mainWindow():
    global main_window
    main_window=Tk()
    main_window.geometry("900x900")
    main_window.title("Algoritmo DES")
    main_window.config(bg="#ffffff")
    main_window.resizable(False, False)
    
    #Fondo de la ventana
    background=Image.open("../resources/background.png")
    background_aux = ImageTk.PhotoImage(background)
    lbl_background=Label(main_window,image=background_aux).place(x=-2,y=-2)

    label = Label(main_window,text="Cifrado de Algoritmo DES", fg="#000000",bg="#c1e8d5",font=('Corbel',20)).place(x=300,y=20)

    label = Label(main_window,text="Ingrese el mensaje:", fg="#000000",bg="#c1e8d5",font=('Corbel',18)).place(x=40,y=80)
    global message
    message=StringVar()
    entry_message=Entry(main_window,textvariable=message,width=40,relief=FLAT, bg="#ffffff",fg="#0ECA9B",font=('Corbel',12)).place(x=45,y=120)

    label = Label(main_window,text="Ingrese la clave:", fg="#000000",bg="#c1e8d5",font=('Corbel',18)).place(x=507,y=80)
    global key
    key=StringVar()
    entry_key=Entry(main_window,textvariable=key,width=40,relief=FLAT, bg="#ffffff",fg="#0ECA9B",font=('Corbel',12)).place(x=512,y=120)

    label = Label(main_window,text="Proceso del algoritmo", fg="#000000",bg="#c1e8d5",font=('Corbel',20)).place(x=150,y=163)
    log = Listbox (main_window,fg="#000000",bg="#ffffff",height=29,width=95)

    # Insert elements into the listbox 
    for values in range(100): 
        log.insert(END, values) 

    log.place(x=159,y=217)

    #Mensaje encriptado
    label = Label(main_window,text="Mensaje encriptado", fg="#000000",bg="#c1e8d5",font=('Corbel',18)).place(x=350,y=710)
    encrypted=StringVar()
    entry_message_encrypted=Text(main_window,height=2,width=52,bg="#ffffff",state=DISABLED,fg="#0ECA9B",font=('Corbel',16)).place(x=157,y=760)

    #botón de play
    img_btn_play=Image.open("../resources/play.png")
    img_resize_btn_play = img_btn_play.resize((30, 30), Image.ANTIALIAS)
    img_btn_play_aux = ImageTk.PhotoImage(img_resize_btn_play)
    btn_play=Button(main_window,bg="white",image=img_btn_play_aux,relief=FLAT,highlightthickness=0, bd=0).place(x=430,y=115)


    main_window.mainloop()

mainWindow()
