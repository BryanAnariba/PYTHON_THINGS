class Persona():
    def __init__(self, __nombrePersona, __apellidoPersona, __edad, __lugar):
        self.__nombrePersona = __nombrePersona
        self.__apellidoPersona = __apellidoPersona
        self.__edad = __edad
        self.__lugar = __lugar

    def setNombrePersona(self, __nombrePersona):
        self.__nombrePersona = __nombrePersona

    def setApellidoPersona(self, __apellidoPersona):
        self.__apellidoPersona = __apellidoPersona

    def setEdad(self, __edad):
        self.__edad = __edad

    def setLugar(self, __lugar):
        self.__lugar = __lugar

    def getNombrePersona(self):
        return self.__nombrePersona

    def getApellidoPersona(self):
        return self.__apellidoPersona
        
    def getEdad(self):
        return self.__edad

    def getLugar(self):
        return self.__lugar

    def getDatosPersona(self):
        return [
            {
                "nombrePersona": self.__nombrePersona,
                "apellidoPersona": self.__apellidoPersona,
                "edadPersona": self.__edad,
                "residenciaActual": self.__lugar
            }
        ]
