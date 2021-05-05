import math
def generaNumeroPotenciado(rangoNumeros):
    num = 1
    listaNumeros = []
    while num <= rangoNumeros:
        listaNumeros.append(math.pow(num,2))
        num = num + 1
    return listaNumeros

def generaNumeroPotenciadoConYield(rangoNumeros):
    num = 1
    while num <= rangoNumeros:
        yield math.pow(num,2)
        num = num + 1


rangoNumeros = int(input("Digite el rango de numeros para poder sacar la potencia al cuadrado: "))
print(generaNumeroPotenciado(rangoNumeros))


rangoNumerosYield = int(input("Digite el rango de numeros para poder sacar la potencia al cuadrado: "))
devuelveRangos = generaNumeroPotenciadoConYield(rangoNumerosYield)

print(next(devuelveRangos))

print("==============")

print(next(devuelveRangos))

print("==============")

print(next(devuelveRangos))