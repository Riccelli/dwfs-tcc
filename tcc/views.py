from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Proposta, Parcela
from .forms import PropostaForm

def home(request):
    return render(request, 'tcc/index.html', {})


def cadastro_proposta(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PropostaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PropostaForm()

        form.fields["programa"].widget.attrs.update({"class": "form-select"})
        form.fields["cliente"].widget.attrs.update({"class": "form-select"})
        form.fields["contrato"].widget.attrs.update({"class": "form-control"})
        form.fields["data_criacao"].widget.attrs.update({"class": "form-control"})

    return render(request, "tcc/proposta.html", {"form": form})
