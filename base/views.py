from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

def inicio(request):
    return render(request, "inicio.html")


def contato(request):
    sucesso = False
    if request.method == "GET":
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Samuel Carlos de Souza',
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "contato.html", contexto)

def reserva(request):
    sucesso = False
    if request.method == "GET":
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "reserva.html", contexto)

