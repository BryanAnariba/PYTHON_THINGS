import math

i = 1
while i <= 10:
    print(f"Entro por { i } vez")
    i = i + 1

print("")
opcion = int(input("============Calculo de raices cuadradas========== \n1 - Realizar Calculo \n2 - Salir\nSeleccione una opcion = "))

while opcion != 2:
    if opcion != 1:
        print("Opcion no valida en el menu")
        opcion = int(input("============Calculo de raices cuadradas========== \n1 - Realizar Calculo \n2 - Salir\nSeleccione una opcion = "))
    else:
        numero = int(input("Digite un numero: "))
        if numero < 0:
            print(f"El numero { numero } es negativo por lo tanto no se valen las raices negativas")
        else:
            print(f"La raiz del numero es { math.sqrt(numero) }")
    opcion = int(input("============Calculo de raices cuadradas========== \n1 - Realizar Calculo \n2 - Salir\nSeleccione una opcion = "))