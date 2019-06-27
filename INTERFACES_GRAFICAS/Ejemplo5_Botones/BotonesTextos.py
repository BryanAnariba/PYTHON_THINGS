from tkinter import *

def codigoBoton():
    nombre.set("Bryan Ariel")
    apellido.set("Sanchez Anariba")




windows = Tk()
windows.title("Ejemplo Botones")
windows.iconbitmap("../Ejemplo1/madara.ico")

miFrame = Frame(windows,width="800",height="640")
miFrame.pack()

nombre=StringVar()#en la funcion codigoBoton
apellido=StringVar()#apellido en la funcion codigoBoton 

labelNombre = Label(miFrame,text="Digite su Nombre:")
labelNombre.grid(row = 0 ,column = 0 , sticky = "e" , padx = 25 , pady = 25)
txtNombres = Entry(miFrame,textvariable = nombre)
txtNombres.grid(row = 0 , column = 1 , padx = 15)
txtNombres.config(justify="center")


labelApellidos = Label(miFrame,text="Digite su Apellido:")
labelApellidos.grid(row=1 , column = 0 , sticky = "e" , padx = 25 , pady = 25) 
txtApellido = Entry(miFrame,textvariable = apellido)
txtApellido.grid(row = 1 , column = 1 , padx = 15)
txtApellido.config(justify = "center")



labelEdad = Label(miFrame,text="Digite su Edad:")
labelEdad.grid(row=2 , column = 0 , sticky = "e" , padx = 25 , pady = 25)
txtEdad = Entry(miFrame)
txtEdad.grid(row = 2 , column = 1 , padx = 15)
txtEdad.config(justify = "center")

labelCarrera = Label(miFrame , text = "Digite la Carrera de Estudio:")
labelCarrera.grid(row = 3 , column = 0 , sticky = "e" , padx = 25 , pady = 25)
txtCarrera = Entry(miFrame) 
txtCarrera.grid(row = 3 , column = 1 , padx = 15) 
txtCarrera.config(justify="center")



#TEXBOX GRANDE CON SCROLL
labelDireccion = Label(miFrame , text="Digite su Direccion Completa:")
labelDireccion.grid(row = 4 , column = 0 , sticky = "e" , padx = 25 , pady = 25)
txtDireccion = Text(miFrame, width = 15 , heigh=7)
scrollDireccion = Scrollbar(miFrame , command = txtDireccion.yview)
scrollDireccion.grid(row = 4 , column = 3 , sticky = "nsew")
txtDireccion.config(yscrollcommand = scrollDireccion.set)
txtDireccion.grid(row = 4 , column = 1)


labelPassword = Label(miFrame , text = "Digite Su Contraseña:")
labelPassword.grid(row = 5 , column = 0 , sticky = "e" , padx = 25 , pady = 25)
txtPassword = Entry(miFrame)
txtPassword.grid(row = 5 , column = 1 , sticky = "e" , padx = 25 , pady = 25)
txtPassword.config(show="*",justify="center")

#AGREGAR BOTTONES
btnEnviar = Button(windows , text = "Enviar Informacion" , command = codigoBoton)
btnEnviar.pack()

#Instruccion a los Botones


windows.mainloop()