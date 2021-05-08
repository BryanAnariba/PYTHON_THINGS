from VehiculoElectrico import VehiculoElectrico
from Vehiculo import Vehiculo
class BicicletaElectrica( Vehiculo, VehiculoElectrico ): #Herencia multiple, solo python posee esto
    pass


def main():
    myBicycle = BicicletaElectrica( "Roja", 2, "Bacini", 20)
    print(myBicycle.getEstadoVehiculo())

main()
