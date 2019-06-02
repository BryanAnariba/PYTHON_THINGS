class Persona():
    def __init__(self , nombre , apellidos , edad , salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad 
        
    
    def retornaDatosPersonas(self):
        print("Nombres: " , self.nombre , "\nApellidos: " , self.apellidos , "\nedad: " , self.edad)

    


class Empleado(Persona):
    def __init__(self , nombre , apellidos , edad , salario ):
        super().__init__(nombre , apellidos , edad , salario)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.salario = salario

    def funcionCalcularAumento(self , salario , porcentaje):
        self.salario = ((salario * porcentaje) + salario)
        print("Su nuevo salario es: " , self.salario)


    def retornaDatosPersonas(self):
        print("Nombres: " , self.nombre , "\nApellidos: " , self.apellidos , "\nedad: " , self.edad , "\nSalario: " , self.salario)



