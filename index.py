#SE IMPORTARON LIBRERIAS
import tkinter
from tkinter import *
#SE CREO LA VENTANA
window = tkinter.Tk()
window.geometry("500x190")
window.title("Examen Final")
#SE CREO UN FRAME
AFrame = Frame(window)
AFrame.pack()
#SE CREARON LOS LABEL, BOTONES Y ENTRY
#LABEL
label1 = tkinter.Label(AFrame, text = "BIENVENIDO", font =("arial",16))
label2 = tkinter.Label(AFrame, text = "Nombre")
label3 = tkinter.Label(AFrame, text = "Apellido")
label4 = tkinter.Label(AFrame, text = "Día")
label5 = tkinter.Label(AFrame, text = "Mes")
label6 = tkinter.Label(AFrame, text = "Año")
label7 = tkinter.Label(AFrame, text = "Acá se verá el resultado de las funciones")
#ENTRY
entryN = tkinter.Entry(AFrame)
entryA = tkinter.Entry(AFrame)
entryDia = Entry(AFrame)
entryMes = Entry(AFrame)
entryAño = Entry(AFrame)
#BOTONES Y ASIGNACION DE FUNCIONES
boton1 = tkinter.Button(AFrame, text = "Función 1")
boton2 = tkinter.Button(AFrame, text = "Función 2")
boton3 = tkinter.Button(AFrame, text = "Función 3")
boton4 = tkinter.Button(AFrame, text = "Función 4")
boton5 = tkinter.Button(AFrame, text = "Función 5")


#SE LES ASIGNO UNA POSICION DENTRO DE LA VENTANA
label1.grid(row = 0, column = 0, columnspan = 6)
label2.grid(row = 1, column = 1, columnspan = 2)
label3.grid(row = 2, column = 1, columnspan = 2)
label4.grid(row = 3, column = 1, columnspan = 2)
label5.grid(row = 4, column = 1, columnspan = 2)
label6.grid(row = 5, column = 1, columnspan = 2)
label7.grid(row = 7, column = 0, columnspan = 6)
entryN.grid(row = 1, column = 3, columnspan = 4, sticky = W + E)
entryA.grid(row = 2, column = 3, columnspan = 4, sticky = W + E)
entryDia.grid(row = 3, column = 3, columnspan = 4, sticky = W + E)
entryMes.grid(row = 4, column = 3, columnspan = 4, sticky = W + E)
entryAño.grid(row = 5, column = 3, columnspan = 4, sticky = W + E)
boton1.grid(row = 6, column = 1)
boton2.grid(row = 6, column = 2)
boton3.grid(row = 6, column = 3)
boton4.grid(row = 6, column = 4)
boton5.grid(row = 6, column = 5)


window.mainloop()