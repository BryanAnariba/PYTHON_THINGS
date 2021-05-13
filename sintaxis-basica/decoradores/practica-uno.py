# funcion decoradora que contiene las dos funciones para compartir cierta cosa
def funcion_decoradora(function_parametro):
    def funcion_interior(*args):
        # Acciones adicionales en comun en la funcion suma y resta
        print("Se esta realizando un calculo")
        function_parametro(*args)
        print("Se realizo un calculo")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print(int(num1) + int(num2))

@funcion_decoradora
def resta(num1, num2):
    print(int(num1) - int(num2))

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


def main():
    suma(7,5)
    resta(10,10)
    potencia(3, 3)

main()

