from django.shortcuts import render


# Create your views here.

#from django.http import HttpResponse

def index(request):
    context = {
        'summa': 12345
    }
    return render (request, 'lotery/index.html', context)

def menu(request):
    context = {
        
    }
    return request (request, 'mainpage/index.html', context)
 
