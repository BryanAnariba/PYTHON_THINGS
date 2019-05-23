#SINNTAXIS

#NOMBRE_DICCIONARIO = {"CLAVE1_TEXTO":VALOR}
diccionario_paises =    {   
                            "Alemania":"Berlin",
                            "Francia":"Paris",
                            "Reino Unido":"Londres",
                            "España":"Madrid"
                        }

#añadir un elemento al diccionario
print(diccionario_paises)
diccionario_paises["Italia"] = "Roma"

#imprimiendo un campo del diccionario de paises
print(diccionario_paises["Francia"])
print(diccionario_paises["Alemania"])
print(diccionario_paises)

#Eliminar un elemento del diccionario
del diccionario_paises["Alemania"]
print(diccionario_paises)

#**************************************
midiccionario = {23:"jordan",33:"juan"}
print(midiccionario)
print(midiccionario[23])
print(midiccionario.keys())#retorna todas las llaves del diccionario
print(midiccionario.values())#retorna todos los valores del diccionario
print(len(midiccionario))