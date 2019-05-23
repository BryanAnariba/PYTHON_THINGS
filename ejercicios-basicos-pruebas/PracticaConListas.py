print("Bienvenido al Sistema de Listas")
print("1- Agregar un elemento a la Lista: ")
print("2- Agregar un elemento a una posicion especifica de la Lista: ")
print("3- Buscar un elemento en especifico en la lista y devolver su pocision: ")
print("4- Comprobar si un Elemento esta en la lista: ")
print("5- Eliminar un elemento de la lista: ")
print("6- Imprimir Lista: ")
print("7- Salir: ")
milista = []
opcion = input("Seleccione una Opcion: ")
opcion = int(opcion)
while(opcion != 7):
    if(opcion == 1):
        dato = input("Digite el elemento que desea ingresar a la lista: ")
        milista.append(dato)
        print("Dato Almacenado Con Exito.......")
    elif(opcion == 2):
        posicion = int(input("Digite la posicion en la que se va a almacenar el dato: "))
        dato = input("Digite el elemento que desea ingresar a la lista: ")
        milista.insert(posicion,dato)
    elif(opcion == 3):
        dato = input("introduzca el dato que desea buscar: ")
        print(milista.index(dato))
        print("Dato Buscado Con Exito!!!!!!!!!")
    elif(opcion == 4):
        dato = input("Digite el Dato para Verificar si esta en la lista")
        print(dato in milista)
        print("Verificada la existencia del Dato con Exito........!")
    elif(opcion == 5):
        dato = input("Digite el dato que desea borrar de la lista")
        milista.remove(dato)
        print("Dato eliminado con exito......")
    elif(opcion == 6):
        print("**********************************************************************************************")
        print(milista)
        print("**********************************************************************************************")
    print("Bienvenido al Sistema de Listas")
    print("1- Agregar un elemento a la Lista: ")
    print("2- Agregar un elemento a una posicion especifica de la Lista: ")
    print("3- Buscar un elemento en especifico en la lista y devolver su pocision: ")
    print("4- Comprobar si un Elemento esta en la lista: ")
    print("5- Eliminar un elemento de la lista: ")
    print("6- Imprimir Lista: ")
    print("7- Salir: ")
    opcion = int(input("Seleccione una Opcion: "))
print("USTED SALIO EXITOSAMENTE........................!")

