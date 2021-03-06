# Generated by Django 2.2.17 on 2020-12-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('profesion', models.CharField(max_length=150, verbose_name='Profesión')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Foto')),
                ('facebook', models.CharField(max_length=400, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=400, verbose_name='Instagram')),
                ('twitter', models.CharField(max_length=400, verbose_name='Twitter')),
                ('whatsapp', models.CharField(max_length=400, verbose_name='Whatsapp')),
                ('youtube', models.CharField(max_length=400, verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
    ]
