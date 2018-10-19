# Generated by Django 2.1.1 on 2018-10-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essentials', '0006_update_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
    ]
