# Generated by Django 2.2.17 on 2020-12-10 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='NoticiaPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('link_youtube', models.CharField(max_length=400, verbose_name='ID de Youtube')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Noticia principal',
                'verbose_name_plural': 'Noticias principales',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=400, null=True)),
                ('twitter', models.CharField(blank=True, max_length=400, null=True)),
                ('youtube', models.CharField(blank=True, max_length=400, null=True)),
                ('instagram', models.CharField(blank=True, max_length=400, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('audio', models.TextField(verbose_name='Link del MP3')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Categoria', verbose_name='Seleccionar categoría')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Noticias',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-created'],
            },
        ),
    ]