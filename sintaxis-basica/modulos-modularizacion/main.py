from modulos.OperacionesMatematicas import OperacionesMatematicas

num1 = input("Write the first number: ")
num2 = input("Write the second number: ")

while num1.isdigit() == False  and num2.isdigit() == False:
    num1 = input("Write the first number: ")
    num2 = input("Write the second number: ")

operacion =  OperacionesMatematicas(num1, num2)
print(operacion.sumar())
print(operacion.restar())
print(operacion.multiplicar())
print(operacion.dividir())

