# Generated by Django 5.2.1 on 2025-06-13 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='primary_color',
            field=models.CharField(default='#040e26', help_text='Primary color in hex format (e.g., #040e26)', max_length=7, validators=[django.core.validators.RegexValidator('^#[0-9A-Fa-f]{6}$', 'Enter a valid hex color code.')]),
        ),
    ]
