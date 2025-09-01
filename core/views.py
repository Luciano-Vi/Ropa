from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def QS(request):
    return render(request,"core/quienes somos.html")

def PF(request):
    return render(request,"core/preguntas frecuentes.html")

def GI(request):
    return render(request,"core/galleria de imagenes.html")
