class VehiculoElectrico():
    def __init__(self):
        self.__autonomia = 100

    def setEstaCargando( self, __estaCargando ):
        self.__estaCargando = __estaCargando

    def getEstaCargando( self ):
        return self.__estaCargando
