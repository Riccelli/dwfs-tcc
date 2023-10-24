from django.forms import ModelForm, SelectDateWidget

from .models import Proposta


class PropostaForm(ModelForm):
    class Meta:
        model = Proposta
        fields = "__all__"
        widgets = {
            "data_criacao": SelectDateWidget(),
        }
