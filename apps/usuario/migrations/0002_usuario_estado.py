# Generated by Django 4.0.6 on 2022-07-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
