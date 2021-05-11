def sumar(num1, num2):
    return int(num1) + int(num2)
    
def restar(num1, num2):
    return int(num1) - int(num2)
    
def multiplicar():
    return int(num1) * int(num2)
    
def dividir(num1, num2):
    try:
        return int(num1) / int(num2)
    except ZeroDivisionError(error):
        return "You can not divide by Zero"