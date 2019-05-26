#SINTAXIS PARA CREAR UNA CLASE
class Coche():
    #Propiedades de los Objetos: por ejemplo un coche tiene un color y ruedas
    largoCoche = 250
    anchoCoche = 120
    ruedas = 4
    enMarcha = False


    #Metodos: son los comportamientos de los objetos , en este caso un coche arranca , frena , acelerar , girar
    #sintaxis de un metodo por ende lleva self obligatoriamente en todos los metodos
    #para hacer referencia a la propiedad de la clase
    def arrancar(self):
        #para cambiar el comportamiento de los objetos se usa SELF y por eso es obligatorio usar esa palabra reservada
        self.enMarcha = True
    
    def estado(self):
        if(self.enMarcha == True):
            return "El Coche si esta en Marcha............"
        else:
            return "El Coche tiene el Estado Inicial............."
    

#INSTANCIAR UNA CLASE tambien llamado EJEMPLARIZAR
myCoche = Coche()
#ACCEDER ALAS Propiedades una vez instanciada la clase
print("El Largo del coche es: " , myCoche.largoCoche)
print("El Ancho del coche es: " , myCoche.anchoCoche)
print("La cantidad de Ruedas son: " , myCoche.ruedas)
print("Esta en Marcha: " , myCoche.enMarcha)
#myCoche.arrancar()
print("Se cambio la propiedad en Marcha: " , myCoche.estado())


