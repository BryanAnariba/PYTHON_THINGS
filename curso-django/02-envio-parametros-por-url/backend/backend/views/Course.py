from django.http import JsonResponse, HttpResponse
import datetime

class Course():
    def __init__(self):
        self.__fechaActual = datetime.datetime.now()

    def getFechaActual(self, request):
        return HttpResponse("<h2>Fecha Actual = {}</h2>".format(str(self.__fechaActual)))

    def getCourse(self, request, courseId): 
        self.courseId = courseId
        return JsonResponse({ "status": 200, "data": "Welcome to {} course".format(self.courseId) })

    def getClassOfCourse(self, request, courseId, classId):
        return JsonResponse({
            "status": 200,
            "data": "Welcome to course with id: {} in the class: {}".format(courseId, classId)
        })
