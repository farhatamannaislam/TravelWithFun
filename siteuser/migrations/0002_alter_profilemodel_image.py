# Generated by Django 4.2.14 on 2024-08-11 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
