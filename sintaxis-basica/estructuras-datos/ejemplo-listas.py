# Listas -> para almacenar datos, para almacenar grandes cantidades de valores 
# son como los arrays en otros lenguajes []
# se puede ir anexando valores dentro de ella, y se exanden infitamente

miLista = [ 1,2,3,4,5,6 ]
listadoPersonas = [ 'Bryan', 'Erick', 'Maria' ]

print(listadoPersonas) # Imprimiento todas las listas
print(listadoPersonas[0]) # Imprimiento un elemento de la lista
print(listadoPersonas[1:3]) # Imprimiento un valor o rangos de elementos de la lista

# Agregas elementos a la lista
listadoPersonas.append("Juan")
print(listadoPersonas)
listadoPersonas.insert(0,"Kevin")
print(listadoPersonas)


