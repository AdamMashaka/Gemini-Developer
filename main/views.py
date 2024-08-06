from django.shortcuts import render
from .models import ExampleModel


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def notse_view(request):
    return render(request, 'notse.html')


