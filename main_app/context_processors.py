from django.utils.translation import gettext_lazy as _
from .models import JinnoSetting, Service

def site_settings(request):
    settings = JinnoSetting.objects.first()
    services = Service.objects.all().values_list('name', flat=True)
    return {
        'site_settings': {
            'email': settings.email if settings and settings.email else 'contact@jinoo.ca',
            'facebook_link': settings.facebook_link if settings and settings.facebook_link else 'https://www.facebook.com/Jinoo_Inc/',
            'x_link': settings.x_link if settings and settings.x_link else '#',
            'instagram_link': settings.instagram_link if settings and settings.instagram_link else '#',
            'website_link': settings.website_link if settings and settings.website_link else 'www.jinoo.ca',
            'company_name': settings.company_name if settings and settings.company_name else 'Jinoo Inc',
            'company_logo': settings.company_logo.url if settings and settings.company_logo else '',
            'slogan': settings.slogan if settings and settings.slogan else '',
            'phone_number': settings.phone_number if settings and settings.phone_number else '+1 416 570 3344',
            'location': settings.location if settings and settings.location else '1072 Abbott Street, Milton, Ontario, Canada, L9T 5P4',
            'google_maps_url': settings.google_maps_url if settings and settings.google_maps_url else 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2892.5054223062602!2d-79.87156591889807!3d43.533505260162435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882b6efe75c37c6b%3A0x2c9494d2d9626995!2s1072%20Abbott%20St%2C%20Milton%2C%20ON%20L9T%205P4!5e0!3m2!1sfr!2sca!4v1692206095897!5m2!1sfr!2sca',
            'services': list(services) if services else [],
        }
    }