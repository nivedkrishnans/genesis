# Generated by Django 2.0.5 on 2018-09-09 19:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration.field_helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrationStatus', models.CharField(choices=[('notyet', 'Not Yet'), ('opened', 'Open'), ('closed', 'Closed')], default='notyet', max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('registrationLink', models.CharField(default='#', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FootprintsRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('teamName', models.CharField(max_length=200)),
                ('teamLeader', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada')], default='English', max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact1', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('contact2', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('participantList', models.TextField()),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LasyaRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('teamName', models.CharField(max_length=200)),
                ('teamLeader', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact1', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('contact2', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('participantList', models.TextField()),
                ('videoFile', models.FileField(null=True, upload_to='fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d', validators=[registration.field_helpers.lasya_file_validation])),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProsceniumRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('teamName', models.CharField(max_length=200)),
                ('teamLeader', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada')], default='English', max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact1', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('contact2', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing', regex='^\\+91\\d{10}$|^0\\d{10}$|^\\d{10}$')])),
                ('participantList', models.TextField()),
                ('videoFile', models.FileField(null=True, upload_to='fp238a576afovpy23mlzra/do9862x0k3pyl5bxnwxkr8/5n61kixjqfk8lbhkxxvw9m/lasya/%Y/%m/%d', validators=[registration.field_helpers.proscenium_file_validation])),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='unknown_name', max_length=127)),
                ('institution', models.CharField(default='unknown_institution', max_length=127)),
                ('place', models.CharField(default='unknown_place', max_length=127)),
                ('contact', models.CharField(default='NO_NUMBER', max_length=20)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('activation_key', models.CharField(default=1, max_length=255)),
                ('email_validated', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userdata_link', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
