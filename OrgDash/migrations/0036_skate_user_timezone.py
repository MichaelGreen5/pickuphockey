# Generated by Django 4.1 on 2023-05-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0035_skate_auto_invites_sent_skate_auto_rosters_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='skate',
            name='user_timezone',
            field=models.CharField(default='UTC', max_length=100, null=True),
        ),
    ]