from django import forms
from .models import Servico, Agenda

class Servicoform(forms.ModelForm):
    class Meta:
        model =Servico
        fields ='__all__'


class Agendaform(forms.ModelForm):
    class Meta:
        model = Agenda
        fields='__all__'