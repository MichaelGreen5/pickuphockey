# Generated by Django 4.1 on 2023-04-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0026_remove_goalie_player_goalie_email_goalie_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goalie',
            name='email',
        ),
        migrations.RemoveField(
            model_name='goalie',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='goalie',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='goalie',
            name='skill',
        ),
        migrations.AddField(
            model_name='goalie',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OrgDash.player'),
        ),
    ]
