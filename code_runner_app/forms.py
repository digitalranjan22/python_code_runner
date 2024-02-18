# code_runner_app/forms.py
from django import forms

class CodeExecutionForm(forms.Form):
    parameters = forms.CharField(widget=forms.Textarea)
