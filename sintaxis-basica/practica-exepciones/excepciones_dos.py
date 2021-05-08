def divideNumbers ():
    try:
        number1 = float(input("Write the first number: "))
        number2 = float(input("Write the first number: "))
        print(f"The Division is: { num1/num2 }")
    except ValueError:
        print("Strings are not valid, please write numbers")
    except ZeroDivisionError:
        print("You can not divide by Zero")
    except:
        print("An error was ocurred")
    finally:
        print("Database close, finally is important for close DataBases Connection")

    print("Continue")

divideNumbers()