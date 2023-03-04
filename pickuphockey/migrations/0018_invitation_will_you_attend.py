# Generated by Django 4.1 on 2023-02-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickuphockey', '0017_delete_guestlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='will_you_attend',
            field=models.CharField(choices=[(1, 'Yes'), (2, 'No'), (3, 'Put me on the waitlist')], default=2, max_length=256),
        ),
    ]