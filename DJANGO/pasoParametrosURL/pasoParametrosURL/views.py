from django.http import HttpResponse

edadActual = int()
periodo = int()
edadFutura = int()


def calcularEdad(request , age , anio) :
    edadActual = age
    periodo = anio - 2019
    edadFutura = edadActual + periodo
    
    documento = """
        <html>
            <body>
                <h2>
                    En el año %s tendras %s años 
                </h2>
            </body>
        </html>
    """ %(age , edadFutura)

    #primer %s -> año enviado por el parametro , segundo %s la edad , el ultimo %(age , edadFutura) va afuera
    return HttpResponse(documento)


    #abrir en http://localhost:8000/edadFutura/23/2032
    #año -> 2070 por ejemplo
    #parsear en url el parametro age a entero ya que los parametros viajan como texto plano y hay que parsearlo a int