#funciones de cadenas pora tamaños o saber la si una direccion de correo es valida
#upper() convierte en mayusculas
#lower() pasa a minusculas
#capitalize() primer letra en mayusculas
#count() cuenta cantidad de letras en una oracion
#split() separa palabras
#replace() reemplaza una oracion por otra

#referencia de biblioteca

nombre = input("Digite su Nombre: ")
print("El nombre es: " , nombre)
print("El nombre en Mayusculas es: " , nombre.upper())
print("El nombre en Minusculas es: " , nombre.lower())
print("El nombre en Primer letra Mayus " , nombre.capitalize())


edad = input("Digite su edad: ")
while(edad.isdigit()==False):
    print("Edad no es digito")
    edad = input("Digite La edad: ")


if(int(edad)<18):
    print("No puede pasar....")
else:
    print("Puede Pasar......")