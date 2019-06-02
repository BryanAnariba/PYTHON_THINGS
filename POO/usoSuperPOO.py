class Personas():
    def __init__(self, nombre , edad , lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcionPersona(self):
        print("Nombre: " , self.nombre , "\nedad: " , self.edad , "\nLugar de Residencia: " , self.lugar_residencia)


class Empleados(Personas):#HERENDANDO DE PERSONA
    def __init__(self,salario,antiguedad,nombreEmpleado,edadEmpleado,residenciaEmpleado):#hay que pasar los atributos de la clase persona a fuerza
        super().__init__(nombreEmpleado,edadEmpleado,residenciaEmpleado)#con super llama al metodo constructor de la clase persona para pasar parametros 
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcionEmpleado(self):
        super().descripcionPersona()#heredamos el metodo descripcionPersona y solo agregamos los parametros restantes
        print("\nSalario: " , self.salario , "\nAntiguedad: " , self.antiguedad)



bryan = Personas("Bryan Ariel Sanchez",22,"Villa Olimpica")
bryan.descripcionPersona()
erick = Empleados(22000 , 5 , "Erick David Jimenez",20,"Col Vistas del Valle")#tamos forzados a mandar dichos parametros de la class persona
erick.descripcionEmpleado()

#uso isinstance para ver si una clase es hija de otra, retorna bool
#es erick un empleado
print(isinstance(erick,Empleados))
print(isinstance(erick,Personas))
#es bryan un empleado
print(isinstance(bryan,Empleados))
    