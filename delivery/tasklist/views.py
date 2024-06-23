from django.shortcuts import render

# Create your views here.

def func_new(request):
    slovar = {'Make work': 20122024,
              'Read book': 11122024,
              'Sent mail': 18122024}
              
    return render(request, 'tasklist/first.html', slovar

    )
           


   
