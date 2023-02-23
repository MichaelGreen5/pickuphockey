# Generated by Django 4.1 on 2023-02-22 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pickuphockey', '0021_alter_invitation_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.TextField(max_length=260)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickuphockey.group')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickuphockey.player')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='players',
            field=models.ManyToManyField(default=None, through='pickuphockey.PlayerGroup', to='pickuphockey.player'),
        ),
    ]
