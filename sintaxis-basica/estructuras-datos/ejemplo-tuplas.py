# Tuplas: son listas inmutables, mas rapidas pero con limitaciones

# Tuplas
tuplaNombreUno = ( 'Bryan', 24, 'Ingeniero en Sistemas' )
tuplaNombreDos = ( 'Maria', 22, 'Abogada' )


# Lista
carrerList = [ 'IS', 'II', 'IQ', 'IM' ]

print(tuplaNombreUno)
print(tuplaNombreUno[0])

# Transformar una tupla en listas
tuplaALista = list(tuplaNombreUno)
print("")
print("Tupla a lista")
print(tuplaNombreUno)
print(tuplaALista)

# Transformar lista a tupla
print("")
print("Lista a tupla")
listaATupla = tuple(carrerList)
print(carrerList)
print(listaATupla)

print("")
print("Busqueda en una tupla, carrera IS")
print("IS" in carrerList)


print("")
print("Count de registros en una tupla")
print(len(tuplaALista))

#Desestructuracion en tupla
tuplaJugador = [ "BmorningStar", 24, 100, 15 ]
nombreJugador, edad, puntaje, juegosJugados = tuplaJugador
print("")
print("Datos desestructurados del jugador: ", 
    "\nNombreJugador: ", nombreJugador, 
    "\nEdad: ", edad, 
    "\nPuntaje: ", puntaje, 
    "\nJuegos Ganados: ", juegosJugados)
