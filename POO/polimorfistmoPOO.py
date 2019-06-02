class coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas................")

class moto():
    def desplazamiento(self):
        print("Me Dezplazo en Dos Ruedas..........")

class camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas..............")



#aqui no se equivoca y cada instancia llama a su respectivo metodo
miVehiculo = moto()
miVehiculo.desplazamiento()
miVehiculo2 = coche()
miVehiculo2.desplazamiento()
miVehiculo3 = camion()
miVehiculo3.desplazamiento()

#pero con esto
def desplazamientoVehiculo(vehiculo):#el parametro vehiculo es el que cambia de forma
    vehiculo.desplazamiento()

miVehiculo4 = camion()
desplazamientoVehiculo(miVehiculo4)#al llamar este metodo con la instancia miVehiculo4 la funcion detecta que es un camion
miVehiculo5 = coche()
desplazamientoVehiculo(miVehiculo5)#al llamar este metodo con la instancia miVehiculo5 la funcion detecta que es un coche