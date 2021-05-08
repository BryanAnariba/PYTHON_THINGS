class Coche:
    def __init__ (self):
        # __ encapsulacion privada
        self.__largoChasis = 250
        self.__anchoChasis = 150
        self.__ruedas = 4
        self.enMarcha = False
        self.__gasolina = True
        self.__aceite = True
        self.__puertas = True

    def setGasolina( self, __gasolina ):
        self.__gasolina = __gasolina
    
    def getGasolina(self):
        return self.__gasolina

    def setAceite( self, __aceite ):
        self.__aceite = __aceite
    
    def getAceite(self):
        return self.__aceite

    def setPuertas( self, __puertas ):
        self.__puertas = __puertas
    
    def getPuertas(self):
        return self.__puertas

    def arrancar (self, __enMarcha):
        self.enMarcha = __enMarcha

    def estaElCocheEnMarcha(self):
        if (self.enMarcha):
            verificaEstadoCoche = self.__chequeoInterno()
            return verificaEstadoCoche
        else:
            return "El coche no esta en marcha"

    # Este metodo debe ser privado solo debe usarse en esta clase
    def __chequeoInterno(self):
        if ( self.__aceite == False and self.__gasolina == True and self.__puertas == True ):
            return "El coche no puede arrancar, por favor revisar el aceite"
        elif ( self.__aceite == False and self.__gasolina == False and self.__puertas == True):
            return "El coche no puede arrancar, por favor revisar la gasolina y el aceite"
        elif ( self.__aceite == False and self.__gasolina == False and self.__puertas == False):
            return "El coche no puede arrancar, por favor revisar las puertas la gasolina y el aceite"
        else:
            return "El coche esta listo para arrancar"

    def retornaDatosCoche (self):
        if (self.enMarcha):
            return f"-Datos del Coche-\nLargo Chasis: { self.__largoChasis }\nAncho Chasis: { self.__anchoChasis }\nCantidad Ruedas: { self.__ruedas }\nEsta en Marcha: Si"
        else:
            return f"-Datos del Coche-\nLargo Chasis: { self.__largoChasis }\nAncho Chasis: { self.__anchoChasis }\nCantidad Ruedas: { self.__ruedas }\nEsta en Marcha: No"