class Vehiculo(object):

    def __init__(self, color, ruedas, marca, modelo):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.enAceleracion = False
        self.enFreno = False
        
    # Setters y Getters

    # Metodos para comportamientos
    def arrancar (self):
        self.enMarcha = True

    def acelerar (self):
        self.enAceleracion = True

    def frenar (self):
        self.enFreno = True

    def getEstadoVehiculo(self):
        return """-Datos Vehiculo- 
            \nMarca: {} 
            \nModelo: {} 
            \nColor: {} 
            \nRuedas: {}
            \nEsta en Marcha: {}
            \nEsta Acelerando: {}
            \nEsta Frenando: {}""".format( 
                self.marca, 
                self.modelo, 
                self.color, 
                self.ruedas, 
                self.enMarcha, 
                self.enAceleracion, 
                self.enFreno 
            )
