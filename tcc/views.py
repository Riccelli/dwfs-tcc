from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Parcela, Aliquota
from .forms import PropostaForm


def gerar_parcelas(prop):
    indice = prop.programa.indice
    modalidade = prop.programa.modalidade.sigla
    valor_principal = prop.valor_principal
    numero_de_parcelas = prop.numero_de_parcelas
    data_criacao = prop.data_criacao
    registro_aliquota = (Aliquota.objects.filter(indice=indice, vigencia__lte=data_criacao)
                         .order_by("-vigencia").first())

    if registro_aliquota is None:
        raise Exception("Alíquota vigente não disponível")
    else:
        # Transforma a taxa anual em mensal
        taxa_mensal = registro_aliquota.aliquota / 12

    if modalidade == 'SAC':
        amortizacao = valor_principal / numero_de_parcelas
        for num in range(numero_de_parcelas):
            parcela = Parcela()
            parcela.proposta = prop
            parcela.numero = num + 1
            parcela.vencimento = data_criacao + relativedelta(months=num + 1)
            parcela.valor = amortizacao + (valor_principal * taxa_mensal)
            parcela.save()
            valor_principal -= amortizacao
    elif modalidade == 'PRICE':
        valor_parcela = ((valor_principal * taxa_mensal * pow(1 + taxa_mensal, numero_de_parcelas))
                         / (pow(1 + taxa_mensal, numero_de_parcelas) - 1))
        for num in range(numero_de_parcelas):
            parcela = Parcela()
            parcela.proposta = prop
            parcela.numero = num + 1
            parcela.vencimento = data_criacao + relativedelta(months=num + 1)
            parcela.valor = valor_parcela
            parcela.save()
    else:
        raise Exception("Modalidade inválida")


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
