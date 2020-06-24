from django.shortcuts import render
from .models import Gallary

def home(request):
    pics = Gallary.objects
    return render(request, 'gallary/home.html',{'pics':pics})

def about(request):
    return render(request, 'gallary/about.html')

def starttracking(request):
    return render(request, 'gallary/starttracking.html')
