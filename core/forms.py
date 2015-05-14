from django import forms 
from models import Cliente,Contrato
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
    	fields = ['nome','sexo','nascimento','rg','cpf','rua','bairro','cidade','estado']
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        exclude = ['consultor']
    