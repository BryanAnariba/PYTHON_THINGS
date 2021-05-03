# Recorriendo STRINGS
for i in ["Javascript","PHP","NodeJS"]:
    print(i, end=", ")

print("")
contador = 0
email = input("Write your email: ")
isEmail = False
for i in email:
    if i == "@" or i == ".":
        contador = contador + 1

if contador >= 2:
    print("")
    print("El email es un correo")
else:
    print("")
    print("El email no es un correo")

# Uso de range en el for -> del 0 al 9 se imprime 10 veses hola
for i in range(10):
    print("Hola")