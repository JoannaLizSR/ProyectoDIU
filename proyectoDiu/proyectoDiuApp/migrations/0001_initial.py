# Generated by Django 4.0.4 on 2022-06-15 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2022, 6, 15, 8, 49, 49, 414305))),
            ],
        ),
    ]
