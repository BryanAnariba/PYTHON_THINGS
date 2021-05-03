# Diccionarios
    # son como los arreglos asociativos en php o objeto en javascript
    # se usa clake: valor
    # Pueden almacenar cualquier tipo de valor hasta listas tuplas e incluso diccionarios


diccionarioEmpleados = [
    {
        "nombre": "Bryan Ariel",
        "cargo": "Web Developer & Mobile Developer",
        "experience": ["Lummina tecnologies", "Becas 2020"]
    },
    {
        "nombre": "Maria Fernanda",
        "cargo": "UI/UX Designer",
        "experience": []
    }
]

diccionarioPaises = [
    "Alemania","Honduras"
]

print(diccionarioEmpleados)
print(diccionarioPaises)
print(len(diccionarioEmpleados))

print("")
print("Datos en for")
for i in diccionarioEmpleados:
    print(i)
    


