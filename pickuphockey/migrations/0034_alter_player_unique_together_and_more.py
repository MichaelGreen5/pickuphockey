# Generated by Django 4.1 on 2023-03-08 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0008_invitation_player_playergroup_skate_and_more'),
        ('pickuphockey', '0033_alter_playergroup_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='player',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='playergroup',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='playergroup',
            name='members',
        ),
        migrations.RemoveField(
            model_name='skate',
            name='host',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='PlayerGroup',
        ),
        migrations.DeleteModel(
            name='Skate',
        ),
    ]
