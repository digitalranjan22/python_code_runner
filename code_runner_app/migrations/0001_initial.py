# Generated by Django 4.1.7 on 2024-02-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code_file', models.FileField(upload_to='python_codes/')),
            ],
        ),
        migrations.CreateModel(
            name='CodeExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('execution_date', models.DateTimeField(auto_now_add=True)),
                ('output', models.TextField()),
                ('python_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_runner_app.pythoncode')),
            ],
        ),
        migrations.CreateModel(
            name='CodeConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_folder', models.CharField(max_length=100)),
                ('output_folder', models.CharField(max_length=100)),
                ('python_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_runner_app.pythoncode')),
            ],
        ),
    ]
