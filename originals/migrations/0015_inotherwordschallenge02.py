# Generated by Django 2.1.1 on 2018-09-29 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('originals', '0014_auto_20180921_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOtherWordsChallenge02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placesOrder', models.CharField(blank=True, max_length=20, null=True)),
                ('question2', models.TextField(blank=True, max_length=400, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify_date', models.DateTimeField(blank=True, null=True)),
                ('submit_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('isSubmit', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
