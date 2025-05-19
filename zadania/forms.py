from django import forms
from .models import Solution

class SolutionUploadForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['code_file']

class SQLSolutionForm(forms.Form):
    solution_text = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':80}))
