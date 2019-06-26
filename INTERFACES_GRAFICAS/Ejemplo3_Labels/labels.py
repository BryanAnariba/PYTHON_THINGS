from tkinter import *

windows = Tk()
windows.title("Ejemplo Labels")
windows.iconbitmap("../Ejemplo1/madara.ico")

Frame = Frame(windows , width="1024" , height="640")

miimagen = PhotoImage(file="Linux.png")

Frame.pack()


#PASOS PARA LA CREACION DE LOS LABELS
miLabel = Label(Frame,text="Label Insertado en Python",fg="Gray",font=("Arial",18)).place(x=20 , y = 10)
miLabel2 = Label(Frame , image = miimagen).place(x=100 , y =100)








windows.mainloop()