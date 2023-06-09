# Generated by Django 4.1 on 2023-03-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickuphockey', '0029_alter_skate_finalize_event_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergroup',
            name='Player',
        ),
        migrations.RemoveField(
            model_name='playergroup',
            name='group',
        ),
        migrations.AddField(
            model_name='playergroup',
            name='members',
            field=models.ManyToManyField(related_name='groups', to='pickuphockey.player'),
        ),
        migrations.AddField(
            model_name='playergroup',
            name='name',
            field=models.CharField(default='Group Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='skate',
            name='frequency',
            field=models.IntegerField(blank=True, choices=[(7, 'Every Week'), (14, 'Every Two Weeks')], default='Every Week'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
