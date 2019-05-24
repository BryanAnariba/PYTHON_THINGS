#ES UN CICLO QUE TIENE UN DETERMINADO NUMERO DE REPETICIONES, PARA OTROS SERIA WHILE O DO WHILE
#FOR ES UN BUCLE DETERMINADO
#WHILE Y DO WHILE SON INDETERMINADOS

#IMPRIMIR 5 VESES HOLA MUNDO GRACIAS AL BUCLE FOR
for i in range(5):
    print("Hello World.......!")


#RELLENAR UNA LISTA CON 5 ELEMENTOS GRACIAS AL BUCLE FOR
milista = []
for i in range(5):
    dato = input("Digite un dato para almacenar en la lista: ")
    milista.append(dato)


#imprimiendo la lista con la funcion normal
print(milista)


#RECORRIENDO UNA LISTA CON BUCLE FOR
for i in milista:
    print(i)


#imprmiendo todo en una linea
for i in ["Bryan","Ariel","Sanchez","Anariba"]:
    print("hola",end=" ")



#RECORRER UN STRING PARA VERIFICAR LA DIRECCION DE CORREO ELECTRONICO VALIDA
contador1 = 0
contador = 0
myemail = input("Digite la direccion de correo electronico: ")
for i in myemail:
    if(i == "@" or i == "."):
        if(i == "@"):
            contador = contador + 1
        if(i == "."):
            contador1 = contador1 + 1

            
if(contador == 1 and contador1 > 0):
    print("Direccion de correo Correcta")
else:
    print("Direccion de correo incorrecta")
