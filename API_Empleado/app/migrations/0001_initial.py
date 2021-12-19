# Generated by Django 4.0 on 2021-12-18 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArea', models.CharField(max_length=100)),
                ('activa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDocumento', models.CharField(max_length=100)),
                ('formato', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSubArea', models.CharField(max_length=100)),
                ('activa', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numDocumento', models.CharField(max_length=25)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.documento')),
                ('subarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subarea')),
            ],
        ),
    ]