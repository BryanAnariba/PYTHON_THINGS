def verificaEsActoParaMencionHonorifica (nota):
    if nota >= 0 and nota < 65:
        return "Eres un burro"
    elif nota >= 65 and nota < 80:
        return "Por lo menos pasaste"
    elif nota >= 80 and nota <= 90:
        return "Buena nota, Cumlaude"
    elif nota >= 90 and nota <= 94:
        return "Excelente nota, magna cumlaude"
    elif nota >= 95 and nota <= 100:
        return "Felicidades, grado maximo, suma cumlaude"
    else:
        return "Opcion no valida, la nota no es correcta"

print(verificaEsActoParaMencionHonorifica(-1))
print(verificaEsActoParaMencionHonorifica(50))
print(verificaEsActoParaMencionHonorifica(75))
print(verificaEsActoParaMencionHonorifica(86))
print(verificaEsActoParaMencionHonorifica(92))
print(verificaEsActoParaMencionHonorifica(98))