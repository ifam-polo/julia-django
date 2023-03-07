from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
import datetime
from .models import Transacao
from .forms import TransacaoForm


def home(request):
    print(f"request transações: {request}")
    return HttpResponse('Hello, World!')
    

def transacao(request):
    data = {}

    data['transacoes'] = ['transacao1', 'transacao2', 'transacao3']
    data['now'] = datetime.datetime.now()
    print(f"request transações: {request}")
    return render(request, 'contas/html.html', data)


def listagem(request):
    data = {}

    data['transacoes'] = Transacao.objects.all()
    print(f"request transações: {request}")
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form

    return render(request, 'contas/form.html', data)
