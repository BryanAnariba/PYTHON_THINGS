#SINTAXIS PARA CREAR UNA CLASE
class Coche():
    #CONSTRUCTOR PARA INICIAR PROPIEDADES Y ASI TENGAN UN ESTADO INICIAL

    def __init__(self):
        #Propiedades de los Objetos: por ejemplo un coche tiene un color y ruedas
        self.__largoCoche = 250
        self.__anchoCoche = 120
        self.__ruedas = 4   #La variable ruedas es un atributo privado asi solo se modifica desde la clase
        self.__enMarcha = False 


    #Metodos: son los comportamientos de los objetos , en este caso un coche arranca , frena , acelerar , girar
    #sintaxis de un metodo por ende lleva self obligatoriamente en todos los metodos
    #para hacer referencia a la propiedad de la clase
    def arrancar(self,arrancamos):
        self.__enMarcha =  arrancamos

        if(self.__enMarcha):
            chekeo = self.__chequeoInterno()#si el auto arranca o esta en marcha que ejecute el metodo chequeoInterno()
        if(self.__enMarcha == True and chekeo == True):
            return "El Coche si esta en Marcha............"
        elif(self.__enMarcha and chekeo == False):
            return "Algo a ido mal en el chequeo y no podemos arrancar....."
        else:
            return "El Coche tiene el Estado Inicial............."
        

        #para cambiar el comportamiento de los objetos se usa SELF y por eso es obligatorio usar esa palabra reservada
        #self.enMarcha = True

    
    def estado(self):
        print("El coche Tiene: " , self.__ruedas , " Ruedas." , "\nUn Ancho de: " , self.__anchoCoche , "\nUn Largo de: " , self.__largoCoche)
    
    

    #metodo encapsulado ya que no es logico que el coche este apagado y el pueda hacer chequeo
    def __chequeoInterno(self):
        print("Realizando Chequeo Interno........")
        self.aceite = False
        self.gasolina = True
        self.puertas = True
        if(self.aceite == True and self.aceite == True and self.aceite == True):
            return True
        else:
            return False

            
#**************************************************************************************************************#
#INSTANCIAR UNA CLASE tambien llamado EJEMPLARIZAR
myAuto = Coche()



print("\n--------------------------CARACTERISTICAS DEL  PRIMER COCHE-------------------------------------")
#ACCEDER ALAS Propiedades una vez instanciada la clase: ojo no se debe de acceder asi ya que da origen a cambio de informacion , por eso se encapsula

#print("El Largo del coche es: " , myAuto.largoCoche)
#print("El Ancho del coche es: " , myAuto.anchoCoche)
#print("La cantidad de Ruedas son: " , myAuto.ruedas)
#print("Esta en Marcha: " , myAuto.enMarcha)

print(myAuto.arrancar(False))
myAuto.estado()


print("\n-------------------------CARACTERISTICAS DEL SEGUNDO COCHE--------------------------------------")
#CREANDO SEGUNDO OBJETO
myAuto2 = Coche()
print("Acontinuacion Creamos el Segundo Objeto: ")

#print("El Largo del coche es: " , myAuto2.largoCoche)
#print("El Ancho del coche es: " , myAuto2.anchoCoche)
#print("La cantidad de Ruedas son: " , myAuto2.ruedas)
#print("Esta en Marcha: " , myAuto2.enMarcha)
print(myAuto2.arrancar(True))
myAuto2.estado()



