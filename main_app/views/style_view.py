# yourapp/views.py
import re
from django.http import HttpResponse
from django.conf import settings
import os

from main_app.models import Theme

def dynamic_css(request):
    theme = Theme.objects.first()
    primary_color = theme.primary_color if theme else '#040e26'
    secondary_color = theme.secondary_color if theme else '#fc5e28'
    css_path = os.path.join(settings.STATICFILES_DIRS[0], 'css', 'style.css')
    
    try:
        with open(css_path, 'r') as file:
            css_content = file.read()
    except FileNotFoundError:
        css_content = "/* Error: style.css not found */"

    pattern_primary = r'(background|background-color|color|border[^:]*):\s*#040e26(\s*!important)?'
    replacement_primary = r'\1: ' + primary_color + r'\2'
    css_content = re.sub(pattern_primary, replacement_primary, css_content, flags=re.IGNORECASE)

    pattern_secondary = r'(background|background-color|color|border[^:]*):\s*#fc5e28(\s*!important)?'
    replacement_secondary = r'\1: ' + secondary_color + r'\2'
    dynamic_css_content = re.sub(pattern_secondary, replacement_secondary, css_content, flags=re.IGNORECASE)

    return HttpResponse(dynamic_css_content, content_type='text/css')