# Generated by Django 4.2.6 on 2023-10-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosDelito',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Año', models.IntegerField()),
                ('Clave_Ent', models.CharField(max_length=4)),
                ('Entidad', models.CharField(max_length=255)),
                ('Bien_juridico_afectado', models.CharField(max_length=255)),
                ('Tipo_de_delito', models.CharField(max_length=255)),
                ('Subtipo_de_delito', models.CharField(max_length=255)),
                ('Modalidad', models.CharField(max_length=255)),
                ('Enero', models.IntegerField()),
                ('Febrero', models.IntegerField()),
                ('Marzo', models.IntegerField()),
                ('Abril', models.IntegerField()),
                ('Mayo', models.IntegerField()),
                ('Junio', models.IntegerField()),
                ('Julio', models.IntegerField()),
                ('Agosto', models.IntegerField()),
                ('Septiembre', models.IntegerField()),
                ('Octubre', models.IntegerField()),
                ('Noviembre', models.IntegerField()),
                ('Diciembre', models.IntegerField()),
                ('Sexo_Averiguacion_previa', models.CharField(max_length=255)),
                ('Rango_de_edad', models.CharField(max_length=255)),
            ],
        ),
    ]
