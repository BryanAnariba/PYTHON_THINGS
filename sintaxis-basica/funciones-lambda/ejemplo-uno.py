# Funcion normal
'''def calculaAreaTriangulo (base, altura):
    return ((base * altura) / 2)'''

# Funcion tradicional
def calculaAreaTriangulo (base, altura):
    return ((base * altura) / 2)
print(calculaAreaTriangulo(20, 40))

# Funcion lambda
areaTriangulo = lambda base, altura: ((base * altura)/2)

alCubo = lambda base, exponente: (base**exponente) 


print(areaTriangulo(20,40))
print(alCubo(5,3))