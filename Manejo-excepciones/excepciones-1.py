def funcionSumar(a,b):
    return a + b

def funcionRestar(a,b):
    return a - b

def funcionMultiplicar(a,b):
    return a * b

def funcionDividir(a,b):
    try:
        return a / b #Se pone el try dentro dela operacion con un except
    except ZeroDivisionError:
        print("No se Puede Dividir Por 0.....")
        return "Operacion Erronea"

while(True):#intenta hacer que digite dos numeros y hasta que lo haga se ejecuta el break y procede con lo demas
    try:
        num1 = float(input("Digite el Primer numero: "))
        num2 = float(input("Digite el Segundo Numero: "))
        break
    except ValueError:
        print("Los Valores introducidos son cadenas de strings y en este caso se necesitan numeros...")

print("Funciones Con numeros:...")
print("1- Sumar 2 Numeros: ")
print("2- Restar 2 Numeros: ")
print("3- Multiplicar 2 Numeros: ")
print("4- Dividir 2 Numeros: ")
opcion = int(input("Digite una Opcion: "))
if(opcion == 1):
    print("La suma es: " , funcionSumar(num1 , num2))
elif(opcion == 2):
    print("La Resta es: " , funcionRestar(num1 , num2))
elif(opcion == 3):
    print("La Multiplicacion es: " , funcionMultiplicar(num1 , num2))
elif(opcion == 4):
    print("La Multiplicacion es: " , funcionDividir(num1 , num2))
else:
    print("Opcion No Valida....")

print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")
print("Aqui va codigo de mentiras...")

