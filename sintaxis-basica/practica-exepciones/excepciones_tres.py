import math

def testAge(edad):
    if edad < 0:
        raise TypeError("Negative ages no permited")
    elif edad < 20:
        return "You are very young"
    elif edad < 40:
        return "You are young"
    elif edad < 65:
        return "You are an adult"
    elif edad < 100:
        return "You are very old"
    
#print(testAge(-15))
print(testAge(15))
print(testAge(35))
print(testAge(66))
print(testAge(99))

def checkRoot(num):
    if num < 0:
        raise ValueError("The number can'nt to be smaller thant Zero")
    else:
        return math.sqrt(num)

try:
    print(checkRoot(4))
    print(checkRoot(-4))
except ValueError as NumberNegative:
    print("The number can'nt to be smaller thant Zero" + NumberNegative)
print("continueeeeee.")
