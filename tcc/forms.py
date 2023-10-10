from django.forms import ModelForm

from .models import Proposta


class PropostaForm(ModelForm):
    class Meta:
        model = Proposta
        fields = "__all__"
        # template_name = "form_snippet.html"
