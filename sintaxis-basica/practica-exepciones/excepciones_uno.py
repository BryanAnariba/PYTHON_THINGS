def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Your can not divide by Zero"
    except:
        return "An error has ocurred"


try:
    op1=(int(input("Write the first number: ")))
    op2=(int(input("Write the second number: ")))	
    operacion=input("Write some of this operations for to watch the result (suma,resta,multiplica,divide)): ")

    if operacion=="suma":
	    print(suma(op1,op2))

    elif operacion=="resta":
        print(resta(op1,op2))

    elif operacion=="multiplica":
        print(multiplica(op1,op2))

    elif operacion=="divide":
        print(divide(op1,op2))

    else:
        print ("Invalid Operation")
except ValueError:
    print("An error was ocurred, please write numbers no strings")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")