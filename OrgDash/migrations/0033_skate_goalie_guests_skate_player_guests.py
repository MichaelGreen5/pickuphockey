# Generated by Django 4.1 on 2023-05-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0032_alter_darkteam_event_alter_lightteam_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='skate',
            name='goalie_guests',
            field=models.ManyToManyField(related_name='goalie_guests', to='OrgDash.player'),
        ),
        migrations.AddField(
            model_name='skate',
            name='player_guests',
            field=models.ManyToManyField(related_name='player_guests', to='OrgDash.player'),
        ),
    ]
