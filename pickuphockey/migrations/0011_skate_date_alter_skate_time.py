# Generated by Django 4.1 on 2023-02-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickuphockey', '0010_remove_skate_host_skate_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='skate',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='skate',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]
