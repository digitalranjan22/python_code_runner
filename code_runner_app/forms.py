# code_runner_app/forms.py
from django import forms

class CodeExecutionForm(forms.Form):
    parameters = forms.CharField(widget=forms.Textarea)

class File1Form(forms.Form):
    file1_input = forms.FileField()
