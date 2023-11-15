from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os
def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time/'),
        'Показать содержимое рабочей директории': reverse('workdir/')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    
    current_time = datetime.datetime().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir_contents = os.listdir()
    response = HttpResponse('<h1>Содержимое рабочей директории:</h1>')
    response.write('<ul>')

    for item in workdir_contents:
        response.write(f'<li>{item}</li>')

    response.write('</ul>')

    return response
