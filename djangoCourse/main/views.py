from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'title': 'main page!'})


def about(request):
    return render(request, 'main/about.html')