# Generated by Django 3.2.16 on 2024-12-05 18:10

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birthday',
            options={'verbose_name': 'День рождения'},
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения'),
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birthday'), name='Unique person constraint'),
        ),
    ]
