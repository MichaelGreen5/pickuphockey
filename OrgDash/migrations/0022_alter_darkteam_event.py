# Generated by Django 4.1 on 2023-04-01 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0021_uploadsheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darkteam',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OrgDash.skate'),
        ),
    ]