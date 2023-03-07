from django.forms import ModelForm
from .models import Transacao
import datetime

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'categoria', 'obs'] 