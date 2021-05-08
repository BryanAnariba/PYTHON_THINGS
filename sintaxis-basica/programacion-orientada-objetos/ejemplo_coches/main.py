from classes.Coche import Coche

def main():
    cocheHonda = Coche()
    cocheKia = Coche()
    cocheHiunday = Coche()
    cocheMitsubishi = Coche()

    # Como los atributos estan encapsulados como privado aunque quieras cambiar no se podra
    cocheKia.__anchoChasis = 123
    cocheKia.__ruedas = 7
    

    cocheHonda.arrancar(False)

    cocheKia.arrancar(True)
    cocheKia.setAceite(False)

    cocheHiunday.arrancar(True)
    cocheHiunday.setAceite(False)
    cocheHiunday.setGasolina(False)

    cocheMitsubishi.arrancar(True)
    

    print("======================OBJETO UNO=======================")
    print(cocheHonda.estaElCocheEnMarcha())
    print(cocheHonda.retornaDatosCoche())
    print("======================OBJETO DOS=======================")
    print(cocheKia.estaElCocheEnMarcha())
    print(cocheKia.retornaDatosCoche())
    print("======================OBJETO TRES=======================")
    print(cocheHiunday.estaElCocheEnMarcha())
    print(cocheHiunday.retornaDatosCoche())
    print("======================OBJETO CUATRO=======================")
    print(cocheMitsubishi.estaElCocheEnMarcha())
    print(cocheMitsubishi.retornaDatosCoche())

main()