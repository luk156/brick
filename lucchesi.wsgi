import os
import sys
sys.stdout = sys.stderr
# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/home/django/stable-env/lib/python2.7/site-packages')

# reload 111
# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
#os.environ['PYTHON_EGG_CACHE'] = '/www/lostquery.com/mod_wsgi/egg-cache'

#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append('/home/django/lucchesidinogino/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lucchesidinogino.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
