# Generated by Django 2.2.17 on 2020-12-11 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías / Géneros',
            },
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('link', models.TextField(verbose_name='Link del MP3')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Canción',
                'verbose_name_plural': 'Canciones',
            },
        ),
    ]
