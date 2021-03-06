# Generated by Django 3.2.5 on 2022-06-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido1', models.CharField(max_length=255)),
                ('apellido2', models.CharField(max_length=255)),
                ('CURP', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=650)),
                ('ine', models.FileField(upload_to='documentos/identificacion')),
                ('passaporte_anterior', models.FileField(blank=True, upload_to='documentos/pasaporte')),
                ('matricula_anterior', models.FileField(blank=True, upload_to='documentos/matricula')),
                ('identifacion_padre', models.FileField(blank=True, upload_to='documentos/padres')),
                ('cita_fecha', models.DateTimeField(blank=True)),
                ('pago', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
