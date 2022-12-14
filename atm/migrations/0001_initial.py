# Generated by Django 4.1.3 on 2022-11-08 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('PinNumber', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.CharField(max_length=16)),
                ('Balance', models.PositiveBigIntegerField()),
                ('Deposit', models.PositiveBigIntegerField()),
                ('Withdraw', models.PositiveBigIntegerField()),
                ('isInserted', models.BooleanField(default=False)),
                ('cardUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm.user')),
            ],
        ),
    ]
