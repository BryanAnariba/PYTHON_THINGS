class OperacionesMatematicas():
    def __init__(self, __num1, __num2):
        self.__num1 = __num1
        self.__num2 = __num2

    def setNum1 (self, __num1):
        self.__num1 = __num1
    
    def getNum1 (self):
        return self.__num1

    def setNum2 (self, __num2):
        self.__num2 = __num2
    
    def getNum2 (self):
        return self.__num2

    def sumar(self):
        return int(self.__num1) + int(self.__num2)
    
    def restar(self):
        return int(self.__num1) - int(self.__num2)
    
    def multiplicar(self):
        return int(self.__num1) * int(self.__num2)
    
    def dividir(self):
        try:
            return int(self.__num1) / int(self.__num2)
        except ZeroDivisionError(error):
            return "You can not divide by Zero"