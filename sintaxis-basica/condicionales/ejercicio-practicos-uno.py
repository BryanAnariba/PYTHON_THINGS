# Crea un programa que pida dos números por teclado. El programa tendrá una función
# llamada “DevuelveMax” encargada de devolver el número más alto de los dos
# introducidos

def determinaNumeroMasAlto(numero1, numero2):
    if numero1 > numero2:
        return "El numero " + str(numero1) + " es mayor"
    elif numero1 < numero2:
        return "El numero " + str(numero2) + " es mayor"
    elif numero1 == numero2:
        return "Numeros iguales"
    else:
        return "Numeros no validos"

print(determinaNumeroMasAlto(1,2))
print(determinaNumeroMasAlto(20,15))
print(determinaNumeroMasAlto(1,1))
print(determinaNumeroMasAlto(-1,-1))

#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
#teclado).

def datosEnLista(nombre, apellido, edad):
    listaPersonas = []
    listaPersonas.append(nombre)
    listaPersonas.append(apellido)
    listaPersonas.append(edad)
    print("Datos persona => " , "\nNombre Persona: " , listaPersonas[0] , "\nApellido Personas: " , listaPersonas[1] , "\nEdad Persona: ", listaPersonas[2])



nombre = input("Digite nombre: ")
apellido = input("Digite apellido: ")
edad = int(input("Digite edad: "))
datosEnLista(nombre, apellido, edad)

print("Listado clases de matematicas -> Calculo, Calculo 2, Vectores y Matrices")
opcion = input("Digite la clase a matricular: ")
asignatura = opcion.lower()
if asignatura in ("calculo","calculo 2","vectores y matrices"):
    print("Te matriculaste en: ", asignatura)
