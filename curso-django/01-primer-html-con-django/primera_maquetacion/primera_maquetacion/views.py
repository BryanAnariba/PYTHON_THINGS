from django.http import HttpResponse, JsonResponse

def primeraPagina( request ):
    return HttpResponse("Hey guys, this is a first app with django")


def despedida( request ):
    return JsonResponse({ "data": "Good bye guys" })