from django import forms
from .models import Language

class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(queryset=Language.objects.all(), label='Język')
