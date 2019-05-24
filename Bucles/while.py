#BUCLE INDETERMINADO

#imprimiendo 10 veses un hola
i = 1
while(i <= 10):
    print("Numero actual" , i)
    i = i + 1



#VERIFICACION DE CUENTAS SI UNO PRESIONA MAS DE 3 INTENTOS CUENTA BLOQUEADA DE LO CONTRARIO ENTRA
centinela = False
intentos = 1
clave = input("Digite La Clave: ")
if(clave == "reverse flash"):
    centinela = True
while(clave != "reverse flash"):
    print("Clave incorrecta ")
    clave = input("Digite la clave: ")
    if(clave == "reverse flash"):
        centinela = True
    if(intentos == 2 and clave != "reverse flash"):
        print("Intentos Maximos ya no puede teclear mas claves.....")
        break
    intentos = intentos + 1


if(centinela):
    print("CLAVE CORRECTA......!")
else:
    print("Cuenta Bloqueada.....")

