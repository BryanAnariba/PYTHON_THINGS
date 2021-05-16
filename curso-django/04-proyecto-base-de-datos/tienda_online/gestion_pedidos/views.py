from django.shortcuts import render

def searchProduct(request):
    return render(request, "buscar-producto.html")