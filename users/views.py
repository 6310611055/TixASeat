from re import template
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

def aboutpage(request):
    return render(request, 'users/about.html')