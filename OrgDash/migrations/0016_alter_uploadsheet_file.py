# Generated by Django 4.1 on 2023-03-29 23:43

import OrgDash.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrgDash', '0015_bench'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsheet',
            name='file',
            field=models.FileField(default=None, upload_to='OrgDash/uploads/', validators=[OrgDash.models.validate_sheet_only]),
        ),
    ]
