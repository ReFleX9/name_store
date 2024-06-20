from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин спортивного питания Home',
        'vitamin': 'vitaminy',
        'kreatin': 'kreatin',
        'zakuska': 'sportivnye-zakuski',
        'all': 'all',
 
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, какой магазин хороший'
    }
    return render(request, 'main/about.html', context)