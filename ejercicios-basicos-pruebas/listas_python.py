#Es el equivalente a arreglos en otros lenguajes de programacion
#permiten almacenar varios valores


#como declarar una lista en python
#nombre_lista = [elemento0,elemento1,elemento2,.....,elementon]

#declaranco e imprimiendo listas por porcionesy completa
lista = ["BRYAN","ARIEL","SANCHEZ","ANARIBA",22,25]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
print(lista)
print(lista[0:3])#imprimiendo una porcion chiquita de la lista
print(lista[2:4])
print(lista[4:])#accediento a los 2 ultimos elementos de la lista

#union de dos listas
milista = [1,2,3,4,5,6]
milista1 = [1,2,3,4,5,6]
milista3 = milista + milista1
print(milista3)

#-----------------------------------------------funciones con listas--------------------------------------------------
#para agregar elementos a la lista
lista.append("agregando nuevo elemento")
print(lista)

#insertar un elementos a cualquier parte de la lista
lista.insert(2,"insertando al cubo dos el elemento nuevo")
print(lista)

#devolver la pocision de un dato en la lista
print(lista.index("SANCHEZ"))

#comprobar si un elemento esta en la lista
print("SANCHEZ" in lista)#retorna true en caso de ayarlo o false en contrario

#Eliminar un elemento de la lista 
lista.remove("SANCHEZ")
lista.pop() #elimina el ultimo registro de la lista
print(lista)