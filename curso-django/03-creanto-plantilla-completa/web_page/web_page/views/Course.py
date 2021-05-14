# from django.http import HttpResponse
# from django.template.loader import get_template
import datetime
from django.shortcuts import render

class Course(object):
    def renderCourse (self, request):
        nombre = "Bryan Ariel"
        apellido = "Sanchez Anariba"
        fechaHoraActual = datetime.datetime.now()
        return render(request, 'course.html', { 
            "nombrePersona": nombre, 
            "apellidoPersona": apellido, 
            "fechaHoraActual": fechaHoraActual 
            })
