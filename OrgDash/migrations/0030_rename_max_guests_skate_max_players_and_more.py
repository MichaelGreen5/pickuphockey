# Generated by Django 4.1 on 2023-04-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0029_rename_is_goalie_player_goalie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skate',
            old_name='max_guests',
            new_name='max_players',
        ),
        migrations.AddField(
            model_name='skate',
            name='max_goalies',
            field=models.IntegerField(default=2),
        ),
    ]
