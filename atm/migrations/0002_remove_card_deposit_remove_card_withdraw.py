# Generated by Django 4.1.3 on 2022-11-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Deposit',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Withdraw',
        ),
    ]
