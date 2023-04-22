# Generated by Django 4.1 on 2023-04-01 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0022_alter_darkteam_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goalie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OrgDash.player')),
            ],
        ),
    ]
