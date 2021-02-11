import math
# Funcion basica
def getHelloWorld():
    print("Hello World")

# Funcion con parametros
def sumarNumeros(num1, num2):
    return int(num1) + int(num2)

# Funcion cuadratica
def funcionCuadratica(a, b, c):
    x1 = ((-b + math.sqrt(math.pow(b,2) - 4*a*c))/2*a);
    x2 = ((-b - math.sqrt(math.pow(b,2) - 4*a*c))/2*a);
    print("Valores de la ecuacion cuadratica -> ( X1 = ", x1, ") , ( X2 = ", x2, ")")

getHelloWorld()
num1 = input("Digite el primer Numero: ")
num2 = input("Digite el segundo numero: ")
suma = sumarNumeros(num1, num2)
print("La suma de los dos numeros es -> ", suma)

funcionCuadratica(1, 0, -36)