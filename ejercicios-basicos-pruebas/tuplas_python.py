#SON LISTAS INMUTABLES ESO SIGNIFICA QUE NO SE PUEDEN MODIFICAR UNA VEZ CREADAS

#SINTAXIS
#nombreTupla = (elemento0 , elemento1 , ........ , elementoN)

tupla = ("Bryan","Ariel","Sanchez","Anariba",1,2.33,3,3)

#imprmiento una posicion de la tupla
print(tupla[2])
print(tupla)

#transformando una tupla en una lista
milista = list(tupla)
print(milista)

#transformando una lista en una tupla
mitupla = tuple(milista)
print(mitupla) 

#metodos que se pueden usar en tuplas
print("Bryan" in mitupla)

#count sirve para contar cuantos elementos del mismo hay en la tupla por ejemplo hay 2 3
print(mitupla.count(3))

#devolver el tamaño de una tupla
print(len(mitupla))

#devolver el indice con tuplas
print(mitupla.index("Bryan"))