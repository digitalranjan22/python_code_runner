# code_runner/urls.py
from django.urls import path
from .views import code_list, execute_code

urlpatterns = [
    path('', code_list, name='code_list'),
    path('execute/<int:code_id>/', execute_code, name='execute_code'),
]
