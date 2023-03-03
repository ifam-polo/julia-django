from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def get(request):
    print(f"request transações: {request}")
    return HttpResponse('Hello, World!')
    

def name(request):
    print(f"request transações: {request}")
    return render(request, 'contas/html.html')
