from Vehiculo import Vehiculo

class Furgoneta( Vehiculo ):
    def setCarga ( self, cargado ):
        self.cargado = cargado

    def getCarga( self ):
        return self.cargado

    def estadoFurgoneta( self ):
        if self.cargado == True:
            return "La furgoneta esta completamente cargada"
        else:
            return "La furgoneta esta completamente cargada"

def main():
    myCar = Furgoneta( 'White', 6, 'Izuzu', 600 )
    myCar.setCarga(True)
    myCar.arrancar()
    print(myCar.estadoFurgoneta())
    print(myCar.getEstadoVehiculo())

main()