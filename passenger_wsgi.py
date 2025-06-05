import sys
import os

# Add the project base directory to sys.path
project_home = '/home/jinooca/web_application_jinoo_production/jinno_site'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the Django settings module (inside jinno_site/jinno_site/)
os.environ['DJANGO_SETTINGS_MODULE'] = 'jinno_site.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
