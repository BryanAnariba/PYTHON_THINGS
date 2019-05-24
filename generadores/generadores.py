#SON COMO FUNCIONES ESPECIALES EL CUAL EN VEZ DE RETURN LLEVA YIEL
#yiel significa que contruye un objeto iterable con los objetos 


#funcion que genera pares con generador
def generadorNumerosPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num = num + 1
    


#imprmiendo la funcion de numeros pares
devuelvePares = generadorNumerosPares(10)

#for i in devuelvePares:
 #   print(i)

#devolver los 3 primeros elementos con generadores
print(next(devuelvePares))

print("Aqui va mas codigo de mentiras.")

print(next(devuelvePares))

print("Aqui va mas codigo de mentiras.")

print(next(devuelvePares))

print("Aqui va mas codigo de mentiras.")

print(next(devuelvePares))

print("Aqui va mas codigo de mentiras.")

print(next(devuelvePares))

print("Aqui va mas codigo de mentiras.")

print(next(devuelvePares))


#YIEL FROM y sus usos
print("")
print("")
print("Uso de YIELD con doble for para arrays bidimencionales")
def devuelveCiudades(*ciudades): #el asteristo es para indicar un numero indeterminado de parametros
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudadesDevueltas = devuelveCiudades("Tegucigalpa","Comayagua","Valle","Yoro","Galicia")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print("")
print("")
print("Uso de YIELD FROM para sustituir a arreglos bidimencionales")
def devuelveCiudades2(*ciudades): #el asteristo es para indicar un numero indeterminado de parametros
    for elemento in ciudades:
        yield from elemento

ciudadesDevueltas2 = devuelveCiudades2("Tegucigalpa","Comayagua","Valle","Yoro","Galicia")
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))
print(next(ciudadesDevueltas2))