#el asterisco significa que no se sabe cuantos argumentos vienen en la tupla *ciudades
def devuelveCiudades(*ciudades): 
    for item in ciudades:
        #for subItem in item:
            yield from item

#def devuelveCiudades(*ciudades): 
#     for item in ciudades:
#         for subItem in item:
#             yield subItem


ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Murcia", "Andorra")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))