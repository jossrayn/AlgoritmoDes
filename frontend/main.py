from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os.path

def mainWindow():
    global main_window
    main_window=Tk()
    main_window.geometry("850x850")
    main_window.title("Algoritmo DES")
    main_window.config(bg="#ffffff")
    main_window.resizable(False, False)
    #Fondo de la ventana
    #fondo=Image.open("../resources/background.png")
    #fondo_aux = ImageTk.PhotoImage(fondo)
    fondo = PhotoImage("../resources/background.png")
    ins_fondo=Label(main_window,image=fondo)#.place(x=-2,y=-2)
    ins_fondo.pack()


mainWindow()
