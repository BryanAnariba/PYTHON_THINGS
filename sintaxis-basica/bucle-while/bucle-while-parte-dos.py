for letra in "Python":
    if letra == "h":
        continue
    else:
        print(letra)

contador = 0;
stringCaracter = "Hola Mundo"
for letra in stringCaracter:
    if letra == " ":
        continue
    else:
        contador += 1

print(f"Letras del string sin el espacion = { contador }")

email = input("Write your email: ")
isEmail = False
for i in email:
    if i == "@":
        isEmail = True
    else:
        continue 

if (isEmail):
    print("Correct email")
else:
    print("Incorrect email")

