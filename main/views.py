from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница',
        'list': ['number 1', 56],
        'is_autentificated': True
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')