class VehiculoElectrico():
    def __init__(self, color, ruedas, marca, modelo):
        super().__init__(color, ruedas, marca, modelo)
        self.__autonomia = 100

    def setEstaCargando( self, __estaCargando ):
        self.__estaCargando = __estaCargando

    def getEstaCargando( self ):
        return self.__estaCargando
    
    def getEstadoElectrico(self):
        if self.__estaCargando == True:
            return "El vehiculo electrico se encuentra cargando"
        else:
            return "El vehiculo electrico no se encuentra cargando"
