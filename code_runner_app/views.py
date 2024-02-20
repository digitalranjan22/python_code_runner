# code_runner_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import PythonCode, CodeExecution
from .forms import CodeExecutionForm
from subprocess import run,PIPE 
import sys
# import request


def code_list(request):
    codes = PythonCode.objects.all()
    return render(request, 'code_list.html', {'codes': codes})

def external(request):
    inp = request.Post.get('parm ')
    out = run(sys.executable,'/home/digitalranjan/workspace/python_code_runner/task_list/test.py')
    return True

# def execute_code(request, code_id):
    # python_code = get_object_or_404(PythonCode, pk=code_id)
    # form = CodeExecutionForm(request.POST or None)
    # if form.is_valid():
    #     parameters = form.cleaned_data['parameters']
    #     # Assuming 'python' is in the system's PATH
    #     command = f'python {python_code.code_file.path} {parameters}'
    #     output = subprocess.getoutput(command)
    #     CodeExecution.objects.create(python_code=python_code, parameters=parameters, output=output)
    #     # Handle output location configuration here if needed

    # return render(request, 'execute_code.html', {'python_code': python_code, 'form': form})
