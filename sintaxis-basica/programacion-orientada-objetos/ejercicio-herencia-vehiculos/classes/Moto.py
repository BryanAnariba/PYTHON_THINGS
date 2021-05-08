from Vehiculo import Vehiculo
class Moto( Vehiculo ):
    __haceCaballito = False
    def setHaceCaballito( self, __haceCaballito ):
        self.__haceCaballito = __haceCaballito

    def getHaceCaballito(self):
        return self.__haceCaballito
        
    def getEstadoVehiculo( self ):
        if self.__haceCaballito == True:
            message = "Esta Haciendo Caballito"
        else:
            message = "No esta Haciendo Caballito"
        return """-Datos Vehiculo- 
            \nMarca: {} 
            \nModelo: {} 
            \nColor: {} 
            \nRuedas: {}
            \nEsta en Marca: {}
            \nEsta Acelerando: {}
            \nEsta Frenando: {}
            \nHace Caballito: {}""".format( 
                self.marca, 
                self.modelo, 
                self.color, 
                self.ruedas, 
                self.enMarcha, 
                self.enAceleracion, 
                self.enFreno, 
                message
            )

def main():
    myFirstModo = Moto( 'Red', 2, 'Italika', 250 )
    myFirstModo.setHaceCaballito(True)
    print(myFirstModo.getEstadoVehiculo())

main()
