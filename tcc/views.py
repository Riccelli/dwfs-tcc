from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import Proposta, Parcela
from .forms import PropostaForm


def gerar_parcelas(prop):
    if prop.modalidade == 'SAC':
        amortizacao = prop.principal / prop.numero_de_parcelas
        pass
    elif prop.modalidade == 'PRICE':
        pass
    else:
        pass


def cadastro_proposta(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PropostaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nova_proposta = form.save()
            # Calcular e gravar parcelas
            gerar_parcelas(nova_proposta)

            return HttpResponseRedirect(str.format("/tcc/proposta/{0}/change", nova_proposta.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PropostaForm()

        form.fields["programa"].widget.attrs.update({"class": "form-select"})
        form.fields["cliente"].widget.attrs.update({"class": "form-select"})
        form.fields["contrato"].widget.attrs.update({"class": "form-control"})
        form.fields["data_criacao"].widget.attrs.update({"class": "form-control"})
        form.fields["valor_principal"].widget.attrs.update({"class": "form-control"})
        form.fields["numero_de_parcelas"].widget.attrs.update({"class": "form-control"})

    return render(request, "tcc/proposta.html", {"form": form})
