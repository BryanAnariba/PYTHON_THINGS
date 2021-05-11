class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


def main():
    honda = Coche()
    italika = Moto()
    isuzu = Camion()

    honda.desplazamiento()
    italika.desplazamiento()
    isuzu.desplazamiento()

    def desplazamientoVehiculo(vehiculo):
        vehiculo.desplazamiento()

    miVehiculo = Camion()
    desplazamientoVehiculo(miVehiculo)
    

main()
