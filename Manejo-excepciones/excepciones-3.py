#CREACION DE EXCEPCIONES PROPIAS
def funcionDevuelveEdad(edad):
    if(edad < 0):
        raise TypeError("No se permiten Edades negativas")
    if(edad < 20):
        print("Eres muy joven.")
    elif(edad < 40):
        print("Eres Joven.")
    elif(edad < 65):
        print("Eres Maduro.")
    elif(edad < 100):
        print("Cuidate.....")

print(funcionDevuelveEdad(18))
print(funcionDevuelveEdad(-15))