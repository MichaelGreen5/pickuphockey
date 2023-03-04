# Generated by Django 4.1 on 2023-02-26 20:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pickuphockey', '0025_remove_invitation_is_attending'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('created_by', 'email')},
        ),
    ]