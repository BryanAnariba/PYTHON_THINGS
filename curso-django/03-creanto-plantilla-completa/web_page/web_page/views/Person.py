# from django.http import HttpResponse
# from django.template.loader import get_template
from django.shortcuts import render
import datetime

class Person(object):
    def __init__(self, __firstName, __lastName):
        self.__firstName = __firstName
        self.__lastName = __lastName

    def setFirstName(self, __firstName):
        self.__firstName = __firstName

    def getFirstName(self):
        return self.__firstName

    def setLastName(self, __lastName):
        self.__lastName = __lastName

    def getLastName(self):
        return self.__lastName

    def getPersonData(self,request):
        fechaHoraActual = datetime.datetime.now()
        projects = []
        return render(request, 'person.html', { 
            "nombrePersona": self.getFirstName(), 
            "apellidoPersona": self.getLastName(), 
            "fechaHoraActual": fechaHoraActual,
            "hobbies": [ "Play Soccer","Watch Anime", "Learn Programming languages" ],
            "projects": projects
            })


    
    # def getPersonData(self,request):
    #     fechaHoraActual = datetime.datetime.now()
    #     projects = []
        #personView = get_template('person.html')
        #personViewRender = personView.render({ 
            # "nombrePersona": self.getFirstName(), 
            # "apellidoPersona": self.getLastName(), 
            # "fechaHoraActual": fechaHoraActual,
            # "hobbies": [ "Play Soccer","Watch Anime", "Learn Programming languages" ],
            # "projects": projects
            # })
        #return HttpResponse(personViewRender)