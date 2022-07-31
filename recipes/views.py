#from django.http import HttpResponse # Retorna um response genérico
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Augusto Fadanelli'})

