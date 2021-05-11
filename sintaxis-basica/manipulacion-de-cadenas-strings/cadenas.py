name = input("Write your name: ")
print(name.upper())
print(name.lower())

opcion = input("Write a number: ")
while opcion.isdigit() == False:
    opcion = input("Incorrect param: \nWrite a number: ")



# Crea un programa que pida introducir una dirección de email por teclado. El programa
# debe imprimir en consola si la dirección de email es correcta o no en función de si esta
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
# ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
# o al final, la dirección también será errónea,
email = input("Write an email: ")
if (email.find("@") == 0):
    print("incorrect email, the emails should not started with @")
elif email.count("@") > 1:
    print("incorrect email, the emails should'nt have 2 @")
else:
    print("Email is correct")
