from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import os.path

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

    scrollbar = Scrollbar(main_window)
    scrollbar.pack(side = RIGHT, fill = BOTH)

    # Insert elements into the listbox 
    for values in range(100): 
        log.insert(END, values) 

    log.place(x=159,y=217)
    # Attaching Listbox to Scrollbar 
    # Since we need to have a vertical  
    # scroll we use yscrollcommand 
    log.config(yscrollcommand = scrollbar.set) 
      
    # setting scrollbar command parameter  
    # to listbox.yview method its yview because 
    # we need to have a vertical view 
    scrollbar.config(command = log.yview) 


    #Mensaje encriptado
    label = Label(main_window,text="Mensaje encriptado", fg="#000000",bg="#c1e8d5",font=('Corbel',18)).place(x=350,y=710)
    encrypted=StringVar()
    entry_message_encrypted=Text(main_window,height=2,width=52,bg="#ffffff",state=DISABLED,fg="#0ECA9B",font=('Corbel',16)).place(x=157,y=760)


    main_window.mainloop()

mainWindow()
