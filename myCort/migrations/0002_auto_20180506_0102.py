# Generated by Django 2.0.5 on 2018-05-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
