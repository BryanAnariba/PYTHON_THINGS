def funcionDivide():
    try:
        op1 = float(input("Digite el Primer numero: "))
        op2 = float(input("Digite el segundo numero: "))
        resultado = float(op1 / op2)
        print("La division es: " , resultado)
    except ValueError:
        print("El valor introducido es erroneo. ")
    except ZeroDivisionError:
        print("No se Puede Dividir Por 0.")
    finally:#siempre se ejecuta sin importar el try 
        print("Calculo Finalizado")

funcionDivide()