# Generated by Django 2.1.5 on 2019-02-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190203_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='grade',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
