# Generated by Django 2.0.5 on 2018-05-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('originals', '0002_articles_mail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='mail_id',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
    ]
