class Empleado ():
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} Que trabaja como: {} Tiene un salario mensual: {}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado('Bryan Ariel', 'Web FullStack developer', 4200),
    Empleado('Erick David', 'Web Dev', 3200),
    Empleado('Maria', 'Web Desing', 2700),
    Empleado('Mario', 'Web Desing', 2200),
]

# Mapeo de salarios para dar una comision del 10% a salarios menores o iguales a 2300
def generaCalculo (empleado):
    if empleado.salario < 2300:
        empleado.salario = empleado.salario * 1.10

    return empleado

listaEmpleadosConComision = map(generaCalculo, listaEmpleados)

for empleado in listaEmpleadosConComision:
    print(empleado)