from django.http import HttpResponse


def index(request):
    return HttpResponse('Работает!')


def second_page(request):
    return HttpResponse('Тоже работает')
