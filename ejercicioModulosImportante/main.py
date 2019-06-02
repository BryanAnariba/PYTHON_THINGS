from classPersona import *

nombre = input("Digite Los Nombres del Empleado: ")
apellidos = input("Digite los apellidos del empleado: ")
edad = int(input("Digite la edad del empleado: "))
salario = float(input("Digite el salario del empleado: "))
Empleado = Empleado(nombre , apellidos , edad , salario)
opcion = int(input("Dicho empleado Merece aumento: \n1-si \n2-no "))
if(opcion == 1):
    aumento = float(input("Digite el porcentaje del aumento del empleado: "))
    aumento = aumento / 100
    Empleado.funcionCalcularAumento(salario , aumento)
else: 
    print("El empleado no merece aumento")

    
print("\n\n*--------------------------IMPRIMIENDO DATOS GENERALES DEL EMPLEADO-----------------------------*\n")
Empleado.retornaDatosPersonas()