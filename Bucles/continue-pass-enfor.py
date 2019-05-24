for letra in "python":
    if letra == "h":
        continue#con ncontinue no imprime la letra h la pasa
    print("viendo la letra: " + letra)

nombre = "Pildoras Informaticas"
contador = 0
for i in nombre:
    if i == " ":
        #si i pasa por la letra h no la cuenta y no almacena un numero en el contador
        continue
    contador = contador + 1

print("La Cantidad de letras es: ",contador)
    
