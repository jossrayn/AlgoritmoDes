from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import os.path

from encriptar import *
from desencriptar import * 

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
    global log
    log = Listbox (main_window,fg="#000000",bg="#ffffff",height=29,width=95)

    log.place(x=159,y=217)

    #Mensaje encriptado
    label = Label(main_window,text="Mensaje encriptado", fg="#000000",bg="#c1e8d5",font=('Corbel',18)).place(x=350,y=710)
    global encrypted
    encrypted=StringVar()
    global entry_message_encrypted
    entry_message_encrypted=Entry(main_window,width=52,textvariable=encrypted,bg="#ffffff",state=DISABLED,fg="#0ECA9B",font=('Corbel',16))

    #botón de desencriptar
    img_btn_back=Image.open("../resources/back.png")
    img_resize_btn_back = img_btn_back.resize((30, 30), Image.ANTIALIAS)
    img_btn_back_aux = ImageTk.PhotoImage(img_resize_btn_back)
    btn_back=Button(main_window,bg="white",image=img_btn_back_aux,relief=FLAT,highlightthickness=0, bd=0,command=lambda:execute(2)).place(x=405,y=115)    

    #botón de encriptar
    img_btn_play=Image.open("../resources/play.png")
    img_resize_btn_play = img_btn_play.resize((30, 30), Image.ANTIALIAS)
    img_btn_play_aux = ImageTk.PhotoImage(img_resize_btn_play)
    btn_play=Button(main_window,bg="white",image=img_btn_play_aux,relief=FLAT,highlightthickness=0, bd=0,command=lambda:execute(1)).place(x=445,y=115)


    main_window.mainloop()

def execute(type):
    if(message.get()!="" and key.get()!=""):
        if (type == 1):
            cypher = Encriptar(key.get(),message.get())
            cypher.main()
            values = cypher.logFile
            # Insert elements into the listbox 
            for value in values: 
                log.insert(END, value) 

            cypher_message = cypher.getMensaje()

            encrypted.set(cypher_message)
            entry_message_encrypted.place(x=157,y=760)
        else:
            descypher = Desencriptar(key.get(),message.get())
            descypher.main()
            values = descypher.logFile
            # Insert elements into the listbox 
            for value in values: 
                log.insert(END, value) 

            cypher_message = descypher.getMensaje()

            encrypted.set(cypher_message)
            entry_message_encrypted.place(x=157,y=760)
        

        key.set("")
        message.set("")

    else:
        messagebox.showerror(title="Error! Espacios incompletos.", message="¨Por favor complete los campos de mensaje y clave.")

mainWindow()
