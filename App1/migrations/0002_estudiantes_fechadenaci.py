# Generated by Django 4.1.5 on 2023-01-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='fechaDeNaci',
            field=models.DateField(default='0000-00-00'),
        ),
    ]
