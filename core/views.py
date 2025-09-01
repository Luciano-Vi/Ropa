from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def QS(request):
    return render(request,"core/Quienes somos.html")

def PF(request):
    return render(request,"core/Preguntas frecuentes.html")

def GI(request):
    return render(request,"core/Galleria de imagenes.html")
