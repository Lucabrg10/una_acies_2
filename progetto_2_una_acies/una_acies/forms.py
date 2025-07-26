from django import forms
from .models import Utenza, Cliente, Lettura, Fattura

class UtenzaForm(forms.ModelForm):
    class Meta:
        model = Utenza
        exclude = ['codice']
        widgets = {
            'data_apertura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_chiusura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'indirizzo': forms.TextInput(attrs={'class': 'form-control'}),
            'citta': forms.TextInput(attrs={'class': 'form-control'}),
            'stato': forms.Select(attrs={'class': 'form-select'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
        }
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['codice']
        widgets = {
            'codice_fiscale': forms.TextInput(attrs={'class': 'form-control'}),
            'ragione_sociale': forms.TextInput(attrs={'class': 'form-control'}),
            'indirizzo': forms.TextInput(attrs={'class': 'form-control'}),
            'citta': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LetturaForm(forms.ModelForm):
    class Meta:
        model = Lettura
        exclude = ['codice']
        widgets = {
            'utenza': forms.Select(attrs={'class': 'form-select'}),
            'fattura': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valore': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        
class FatturaForm(forms.ModelForm):
    class Meta:
        model = Fattura
        exclude = ['codice']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'imponibile': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'totale': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }