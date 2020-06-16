from django.shortcuts import render
from .models import Gallary

def home(request):
    pics = Gallary.objects
    return render(request, 'gallary/home.html',{'pics':pics})
