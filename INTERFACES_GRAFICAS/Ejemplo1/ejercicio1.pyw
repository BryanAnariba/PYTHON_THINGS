from tkinter import *

ventana = Tk()

ventana.title("Primer Ejercicio")   #poner titulo a la ventana

ventana.resizable(1,1)  #Redimensionar el tamaño de una ventana 1 true 0 false width , height

ventana.geometry("1024x640")    #tamaño de pantalla

ventana.config(bg="background.jpg")

ventana.iconbitmap("madara.ico") #ponerle un icono a la Ventana

ventana.mainloop()  #bucle infinito que muestra la ventana