from django.http import HttpResponse
from django.shortcuts import render

def homepage(requset):
    return render(requset, 'home.html')

def about(request):
    return render(request, 'about.html')