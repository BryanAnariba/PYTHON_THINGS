class Empleado ():
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} Que trabaja como: {} Tiene un salario mensual: {}".format(self.nombre, self.cargo, self.salario)


listaEmpleado = [
    Empleado('Bryan Ariel', 'Web FullStack developer', 4200),
    Empleado('Erick David', 'Web Dev', 3200),
    Empleado('Maria', 'Web Desing', 2700),
    Empleado('Mario', 'Web Desing', 2200),
]

# Filtrado de salarios mayores a 3000 dolares
salarios = filter(lambda empleado: empleado.salario > 3000, listaEmpleado)

for empleado in salarios:
    print(empleado)