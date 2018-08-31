# Generated by Django 2.0.5 on 2018-08-29 19:26

import django.core.validators
from django.db import migrations, models
import registration.customfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20180830_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lasyaregistration',
            name='videoFile',
            field=models.FileField(blank=True, null=True, upload_to='fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya', validators=[registration.customfields.lasya_file_validation, django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]
