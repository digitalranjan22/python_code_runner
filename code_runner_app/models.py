# code_runner_app/models.py
from django.db import models

class PythonCode(models.Model):
    name = models.CharField(max_length=100)
    code_file = models.FileField(upload_to='python_codes/')

class CodeConfiguration(models.Model):
    python_code = models.ForeignKey(PythonCode, on_delete=models.CASCADE)
    input_folder = models.CharField(max_length=100)
    output_folder = models.CharField(max_length=100)
    # Add other configuration fields as needed

class CodeExecution(models.Model):
    python_code = models.ForeignKey(PythonCode, on_delete=models.CASCADE)
    parameters = models.TextField()
    execution_date = models.DateTimeField(auto_now_add=True)
    output = models.TextField()
