import math
def sumarNumeros (num1, num2):
    return int(num1) + int(num2)

def restarNumeros (num1, num2):
    return int(num1) - int(num2)

def multiplicarNumeros (num1, num2):
    return int(num1) * int(num2)

def dividirNumeros (num1, num2):
    return num1/num2
    
def moduloNumeros (num1, num2):
    return num1%num2

def potenciaNumero (num1):
    return math.pow(num1, 2)

def raizNumero(num1):
    return math.sqrt(num1)

print("Suma -> ", sumarNumeros(5,5))
print("Resta -> ", restarNumeros(5,5))
print("Multiplicacion -> ", multiplicarNumeros(5,5))
print("Division -> ", dividirNumeros(5,5))
print("Modulo -> ", moduloNumeros(5,3))
print("Potencia Cuadrado -> ", potenciaNumero(5))
print("Raiz Cuadrado -> ", raizNumero(25))
