for i in range(10):
    print(f"Numero: { i } al cuadrado : { i * i }")

for i in range( 7, 10 ):
    print(f"Empezamos del 7 al 9, ahorita estamos en el valor : { i }")

isEmail = False
email = input("Write your email: ")
for i in range(len(email)):
    if email[i] == "@":
        isEmail = True

if isEmail:
    print("Email Correct") 
else: 
    print("Email Incorrect")
