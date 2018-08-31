# Generated by Django 2.0.5 on 2018-08-29 18:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration.customfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationActive', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=280)),
                ('registrationLink', models.URLField(default='#')),
            ],
        ),
        migrations.CreateModel(
            name='lasyaRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(default=models.DateTimeField(auto_now_add=True))),
                ('teamName', models.CharField(max_length=200)),
                ('teamLeader', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact1', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('contact2', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('participantList', models.TextField()),
                ('videoFile', models.FileField(blank=True, null=True, upload_to='fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya', validators=[registration.customfields.lasya_file_validation])),
                ('event', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='registration.AdminEvents')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userdata',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
