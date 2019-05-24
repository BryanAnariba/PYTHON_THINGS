print("Verificacion de Acceso")
edad_usuario = int(input("Digite la Edad Del Usuario: "))
if(edad_usuario <= 18):
    print("No Puedes Pasar....")
elif(edad_usuario >= 100):
    print("Edad Incorrecta")
else:
    print("Puedes Pasar.....")
print("Programa Finalizado!")

#ELIF ES COMO ELSE IF EN OTROS LENGUAJES DE PROGRAMACION

#Ejercicio que devuelve el mayor numero de dos ingresados
numero1 = float(input("Digite el Primer numero: "))
numero2 = float(input("Digite el Segundo numero: "))
if(numero1 > numero2):
    print("El numero mayor es: ",numero1)
elif(numero1 < numero2):
    print("El numero mayor es: ",numero2)
elif(numero1 == numero2):
    print("Los Numeros son Iguales")

#Pedir nombre, direccion y telefono e ingresarlos en una lista y luego mostrar la lista con los datos almacenados
milista = []
nombre = input("Digite El Nombre de Usuario: ")
milista.append(nombre)
direccion = input("Digite La Direccion O Residencia: ")
milista.append(direccion)
telefono = input("Digite el Telefono de Usuario: ")
milista.append(telefono)
midiccionario = {"Nombre Usuario: ": milista[0], "Direccion o Residencia Actual: ": milista[1], "Telefono: ": milista[2]}
print(midiccionario)

#MEDIA ARITMETICA DE 3 NUMEROS
num1 = float(input("Digite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))
num3 = float(input("Digite el tercer numero: "))
avg_aritmethic = float((num1+num2+num3)/3)
print("La media aritmetica es: ",avg_aritmethic)

#and y or en if condicionales
#proporcionar beca para alumnos que vivan a mas de 40 km de la escuela
#tenga mas de 2 hermanos
#salario familiar inferior a 20000
#NO SE TIENEN QUE CUMPLIR LAS 3 NECESARIAMENTE
print("-------------------------------Programa de BECAS-----------------------------")
distancia = float(input("Digite La Distancia a la que se encuentra del centro: "))
hermanos = float(input("Digite La cantidad de hermanos que tiene: "))
salario_familiar = float(input("Digite el salario mensual de su familia: "))
if(distancia > 40 or hermanos > 2 or salario_familiar <=20000):
    print("Usted tiene derecho a Beca......")
else:
    print("Usted no tiene derecho a beca.......")



#ASGINATURAS OPTATIVAS AÑO 2019
print("Listado de Clases")
deccionario = {"Informatica Grafica":" if-905","Pruebas de Software":" if-906","Usabilidad y Accesibilidad":" is-907"}
print(deccionario)
asginatura = input("Digite la Asignatura a Cursar: ")
asginatura2 = asginatura.lower()
if(asginatura2 in deccionario):
    print("Asignatura Matriculada con Exito........")
else:
    print("No se encuentran Coincidencias!")