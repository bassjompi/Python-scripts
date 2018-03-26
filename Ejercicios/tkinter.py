from Tkinter import *
import time


def imprime():
    print(nombre)


ventana = Tk()
nombre = StringVar()
ventana.title("quiero coca")
ventana.geometry('400x400')


etiqueta1 = Label(ventana, textvariable=nombre, text='Por favor elija una opcion').place(x=1,y=30)
nombreCaja = Entry(ventana).place(x=200,y=30)
etiqueta2 = Label(ventana,text='Por favor inserte el nombre del archivo').place(x=100,y=60)
ventana.mainloop()