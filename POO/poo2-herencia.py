class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estadoVehiculo(self):
        print("Marca Vehiculo: " , self.marca , "\nModelo Vehiculo: " , self.modelo , "\nEl Vehiculo esta en Marcha: " , self.enMarcha , "\nEl Vehiculo esta en Aceleracion: " , self.acelera , "\nEl Vehiculo Frena: " , self.frena)

#HERENCIA EN PYTHON FUNCIONA ASI , NO ES COMO EN JAVA
class Moto(Vehiculos):
    #metodo caballito ya que solo las motos lo hacen o es recomendable que solo las motos lo hagan
    haceCaballito = ""
    def caballito(self):
        self.haceCaballito = "Voy Haciendo Caballito.............!"

    #sobreescritura de metodos de arriba en este caso el de estadoVehiculo y lo modificamos en Moto class
    def estadoVehiculo(self):
        print("Marca Vehiculo: " , self.marca , "\nModelo Vehiculo: " , self.modelo , "\nEl Vehiculo esta en Marcha: " , self.enMarcha , "\nEl Vehiculo esta en Aceleracion: " , self.acelera , "\nEl Vehiculo Frena: " , self.frena , "\nHace Caballito: " , self.haceCaballito)

#CLASE FURGONETA HEREDANDO DE VEHICULOS
class Furgoneta(Vehiculos):
    def carga(self , capacidadCarga):
        self.cargado = capacidadCarga
        if(self.cargado):
            return "La Furgoneta esta Cargada......!"
        else:
            return "La Furgoneta esta Cargada......!"

#CLASE ELECTRICOS HEREDANDO DE VEHICULOS
class vehiculosElectricos(Vehiculos):
    def __init__(self,marca,modelo):#tanto en super como en el constructor principal hereda los atributos marca y modelo
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

#CLASE ELECTRICOS HEREDANDO DE VEHICULOS:::::::::::::::::::> OJO AQUI SE VE LA HERENCIA MULTIPLE , SOLO PYTHON LA POSE, JAVA NO
class bicicletaElectrica(vehiculosElectricos , Vehiculos):
    pass

#AQUI SE INSTANCIA Y SI EJECUTAS VERAS COMO HEREDA LAS PROPIEDADES DE VEHICULO Y TAMBIEN TIENE LAS PROPIAS
print("")
print("")
print("***********************************************DATOS MOTO************************************************")
Moto_1 = Moto("ITALIKA","RPM")
Moto_1.estadoVehiculo()
Moto_1.caballito()
Moto_1.estadoVehiculo()


print("")
print("")
print("***********************************************DATOS FURGONETA************************************************")
miFurgoneta = Furgoneta("Toyota","RUNNER")
miFurgoneta.arrancar()
miFurgoneta.estadoVehiculo()
print(miFurgoneta.carga(True))


print("")
print("")
print("***********************************************VEHICULO ELECTRICO************************************************")




print("")
print("")
print("***********************************************BICICLETA ELECTRICO************************************************")
bicicleta = bicicletaElectrica("renault","fs-500")#aqui hay dos constructores el que se elige es :::::> el que pones de primero en la extension de la herencia aunque si se puede usar el segundo constructor por ejemplo en el primero hay dos parametros que pasar