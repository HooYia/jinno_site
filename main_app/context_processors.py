from django.utils.translation import gettext_lazy as _
from .models import JinnoSetting

def site_settings(request):
    settings = JinnoSetting.objects.first()
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
        }
    }