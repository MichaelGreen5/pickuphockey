# Generated by Django 4.1 on 2023-02-14 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pickuphockey', '0014_remove_player_user_player_email_player_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]