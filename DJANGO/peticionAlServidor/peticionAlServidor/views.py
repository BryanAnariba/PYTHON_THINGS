from django.http import HttpResponse
import datetime

#importamos http para respuesta y creamos la funcion con su preticion o request
#cada funcicion creada en python es una VISTA.
def devuelveDatos(request):
    return HttpResponse("Respuesta del servidor de parte del backend -> Bienvenido a Python")#respuesta al usuario

def operacionesMatematicas(request):
    cadena = "<h1>Suma  ->  10 "+"\nResta ->  0"+"\nMultiplicacion -> 25</h1>"
    return HttpResponse(cadena)

#luego se hara uso de urls.py -> PARA ENLAZAR LA VISTA CON LOS ENLACES DEL SITIO WEB
#A CONTINUACION IR A URL y despues de establecer los parametros
#ejecutamos
#       python manage.py runserver
#       localhost:8000/respuestaDePrueba


#CREANDO CONTENIDO DINAMICO

def retornaFecha(request):
    fecha_actual = datetime.datetime.now()
    cadena = """
                <body>
                    <h2>Fecha y Hora Actual -> %s </h2>
                </body>
            """% fecha_actual
    return HttpResponse(cadena)

