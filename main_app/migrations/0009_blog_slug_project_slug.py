# Generated by Django 5.2.1 on 2025-06-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_blog_description_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique slug for the blog post URL', max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique slug for the project URL', max_length=250, null=True, unique=True),
        ),
    ]
