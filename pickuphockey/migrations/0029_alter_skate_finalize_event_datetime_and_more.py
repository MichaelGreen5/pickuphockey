# Generated by Django 4.1 on 2023-03-03 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pickuphockey', '0028_skate_finalize_event_datetime_skate_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skate',
            name='finalize_event_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='skate',
            name='frequency',
            field=models.CharField(blank=True, choices=[(7, 'Every Week'), (14, 'Every Two Weeks')], default='Every Week', max_length=256),
        ),
        migrations.AlterField(
            model_name='skate',
            name='send_invites_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
