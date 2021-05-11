from Persona import Persona
class Empleado(Persona):
    def __init__(self, __salario, __cargo, __antiguedad, __nombrePersona, __apellidoPersona, __edad, __lugar):
        super().__init__(__nombrePersona, __apellidoPersona, __edad, __lugar)
        self.__salario = __salario
        self.__cargo = __cargo
        self.__antiguedad = __antiguedad
    
    def getDatosPersona(self):
        return "Datos como Persona: \n{} \nDatos como Empleado: \nSalario {} \nCargo: {} \nAnios Laborando: {} anios".format(super().getDatosPersona(), self.__salario, self.__cargo, self.__antiguedad )
        

bryan = Empleado(1400 ,'Web Developer', 2, 'Bryan Ariel', 'Sanchez Anariba', 24, 'Comayagua')
print(bryan.getDatosPersona())
