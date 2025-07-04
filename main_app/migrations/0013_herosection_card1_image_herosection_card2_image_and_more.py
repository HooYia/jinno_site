# Generated by Django 5.2.1 on 2025-06-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_theme_secondary_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosection',
            name='card1_image',
            field=models.ImageField(blank=True, help_text='Image for the first card in the hero section', null=True, upload_to='hero_cards/'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='card2_image',
            field=models.ImageField(blank=True, help_text='Image for the second card in the hero section', null=True, upload_to='hero_cards/'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='card3_image',
            field=models.ImageField(blank=True, help_text='Image for the third card in the hero section', null=True, upload_to='hero_cards/'),
        ),
        migrations.AddField(
            model_name='servicessectiontwo',
            name='icon_image1',
            field=models.ImageField(blank=True, help_text='Image for the first card in the hero section', null=True, upload_to='services_images/'),
        ),
        migrations.AddField(
            model_name='servicessectiontwo',
            name='icon_image2',
            field=models.ImageField(blank=True, help_text='Image for the first card in the hero section', null=True, upload_to='services_images/'),
        ),
    ]
