# Generated by Django 2.0.5 on 2018-09-01 16:09

from django.db import migrations, models
import registration.customfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20180901_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lasyaregistration',
            name='videoFile',
            field=models.FileField(null=True, upload_to='fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya', validators=[registration.customfields.lasya_file_validation]),
        ),
    ]
