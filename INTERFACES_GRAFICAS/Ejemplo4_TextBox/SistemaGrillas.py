from tkinter import *


windows = Tk()
windows.title("Ejemplo con Text Box")
windows.iconbitmap("../Ejemplo1/madara.ico")

miFrame = Frame(windows,width="800",height="640")
miFrame.pack()

#CREANDO TEXBOXT con labels
labelNombre = Label(miFrame,text="Digite su Nombre: ")
labelNombre.grid(row = 0 , column = 0 , sticky = "e" , padx = 10 , pady=10) #(row,columnas) aqui fila 0 columna 0
txtNombres = Entry(miFrame)
txtNombres.grid(row = 0, column = 1 , padx = 15)
txtNombres.config(justify="center")



labelApellido = Label(miFrame,text="Digite su Apellido: ")
labelApellido.grid(row = 1 , column = 0 , sticky = "e" , padx = 10 , pady=10)
txtApellidos = Entry(miFrame)
txtApellidos.grid(row = 1 , column = 1 , padx = 15)
txtApellidos.config(justify="center")




labelEdad = Label(miFrame,text="Digite su Edad: ")
labelEdad.grid(row = 2 , column = 0 , sticky = "e" , padx = 10 , pady=10)
txtEdad = Entry(miFrame)
txtEdad.grid(row = 2 , column = 1 , padx = 15)
txtEdad.config(justify="center")


labelCarrera = Label(miFrame,text="Digite la Carrera de Estudio: ")
labelCarrera.grid(row = 3 , column = 0 , sticky = "e" , padx = 10 , pady=10)
txtCarrera = Entry(miFrame)
txtCarrera.grid(row = 3 , column = 1 , padx = 15)
txtCarrera.config(justify="center")

labelPassword = Label(miFrame,text="Digite su Contraseña: ")
labelPassword.grid(row = 4 , column = 0, sticky = "e" , padx = 10 , pady = 10)
txtPassword = Entry(miFrame)
txtPassword.grid(row = 4 , column = 1 , padx = 15)
txtPassword.config(justify = "center")
txtPassword.config(show="*")

windows.mainloop()