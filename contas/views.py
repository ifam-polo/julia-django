from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def get(request):
    return HttpResponse('Hello, World!')

def name(request):
    return render(request, 'contas/html.html')
