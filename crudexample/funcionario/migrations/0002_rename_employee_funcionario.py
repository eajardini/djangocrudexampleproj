# Generated by Django 3.2.16 on 2023-10-20 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Funcionario',
        ),
    ]
