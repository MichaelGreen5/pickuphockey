# Generated by Django 4.1 on 2023-02-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickuphockey', '0019_alter_invitation_will_you_attend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skate',
            name='participants',
        ),
        migrations.AddField(
            model_name='skate',
            name='max_guests',
            field=models.IntegerField(default=0),
        ),
    ]
