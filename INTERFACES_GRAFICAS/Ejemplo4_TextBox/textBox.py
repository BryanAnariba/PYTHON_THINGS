from tkinter import *


windows = Tk()
windows.title("Ejemplo con Text Box")
windows.iconbitmap("../Ejemplo1/madara.ico")

miFrame = Frame(windows,width="800",height="640")
miFrame.pack()

#CREANDO TEXBOXT
labelNombre = Label(miFrame,text="Digite su Nombre")
labelNombre.place(x=10 , y=20)
txtNombre = Entry(miFrame)
txtNombre.place(x=120 , y=20)

windows.mainloop()