from VehiculoElectrico import VehiculoElectrico
from Vehiculo import Vehiculo
class BicicletaElectrica( VehiculoElectrico, Vehiculo ): #Herencia multiple, solo python posee esto
    pass


def main():
    myBicycle = BicicletaElectrica( "Roja", 2, "Bacini", 20)
    print(myBicycle.getEstadoVehiculo())
    myBicycle.setEstaCargando(True)
    print(myBicycle.getEstadoElectrico())
    
main()
