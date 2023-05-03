# Generated by Django 4.1 on 2023-05-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OrgDash', '0032_alter_darkteam_event_alter_lightteam_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickLightTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.FloatField(default=0)),
                ('team', models.ManyToManyField(to='OrgDash.player')),
            ],
        ),
        migrations.CreateModel(
            name='QuickDarkTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.FloatField(default=0)),
                ('team', models.ManyToManyField(to='OrgDash.player')),
            ],
        ),
        migrations.CreateModel(
            name='QuickBench',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bench_members', models.ManyToManyField(to='OrgDash.player')),
            ],
        ),
    ]
