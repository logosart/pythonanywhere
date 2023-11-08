from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def materias(request):
    return render(request, "materias.html")

def poo(request):
    return render(request, "poo.html")

def redes(request):
    return render(request, "redes.html")