# Generated by Django 4.2.1 on 2023-06-04 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name', max_length=200)),
                ('last_name', models.CharField(help_text='Enter last name', max_length=200)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(help_text='Enter phone number', max_length=50)),
            ],
        ),
    ]
