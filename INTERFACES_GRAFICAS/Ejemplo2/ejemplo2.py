from tkinter import *

ventana = Tk()
ventana.title("Ejemplo 2 Interfaces Graficas")
ventana.geometry("1024x640")
ventana.iconbitmap("../Ejemplo1/madara.ico")
#ventana.config(bg="Blue")


#CREAR UN FRAME PARA BOTONES , TEXTBOX ,ETC
#PASOS BASICOS PARA UN FRAME
miFrameDentroDeVentana = Frame()
miFrameDentroDeVentana.config(bg="gray")
miFrameDentroDeVentana.config(width="800",height="640")
#miFrameDentroDeVentana.pack(side="bottom" ,anchor="n")     ojo
miFrameDentroDeVentana.pack()#(fill="x") para redimensionar en x , tambien (fill="both",expand="True")


#PASOS PARA PONER UN MARCO EN EL FRAME
#miFrameDentroDeVentana.config(bd="22")
#miFrameDentroDeVentana.config(relief="groove")

#PASOS PARA CAMBIAR EL ICONO DEL MOUSE O CURSOR
miFrameDentroDeVentana.config(cursor="hand2")



#ESTAS PROPIEDADES SIRVEN EN LA VENTANA TAMBIEN SIN NINGUN PROBLEMA
ventana.mainloop()