from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime


def get(request):
    print(f"request transações: {request}")
    return HttpResponse('Hello, World!')
    

def name(request):
    data = {}

    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    print(f"request transações: {request}")
    return render(request, 'contas/html.html', data)
