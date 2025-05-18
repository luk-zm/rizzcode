from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Language

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class LanguageForm(forms.Form):
    language = forms.ModelChoiceField(queryset=Language.objects.all(), label='Język')
