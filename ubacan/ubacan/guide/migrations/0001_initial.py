# Generated by Django 2.1.5 on 2019-02-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tramites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tarea', models.CharField(max_length=50)),
                ('descripcion_tarea', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
