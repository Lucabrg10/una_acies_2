from django import forms
from .models import Utenza

class UtenzaForm(forms.ModelForm):
    class Meta:
        model = Utenza
        exclude = ['codice']
        widgets = {
            'data_apertura': forms.DateInput(attrs={'type': 'date'}),
            'data_chiusura': forms.DateInput(attrs={'type': 'date'}),
        }
