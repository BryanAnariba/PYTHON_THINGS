import re

cadena = "Vamoa a aprender expresiones regulares en Python, Python es un lenguaje Easy"

# expresion para saber si hay una palabra en un string

if (re.search("aprender", cadena) != None):
    print("Hay coincidencia")
else:
    print("no hay coincidencia")


countPythonPhrase = re.findall('Python', cadena)

print(len(countPythonPhrase))

lista_nombres = [
    "Bryan Anariba",
    "Maria Anariba",
    "Erick Anariba",
    "Juan Anariba",
    "Maria De Los Angeles"
]

# ^ para ver cual nombre comienza por maria, y $ los que terminan en Anariba
print("^ para ver cual nombre comienza por maria")
for i in lista_nombres:
    if (re.findall("^Maria", i)):
        print(i)

print("$ los que terminan en Anariba")
for i in lista_nombres:
    if (re.findall("Anariba$", i)):
        print(i)