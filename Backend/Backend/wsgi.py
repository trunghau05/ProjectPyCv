"""
WSGI config for Backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys  # <--- BƯỚC 1: IMPORT THƯ VIỆN SYS
from django.core.wsgi import get_wsgi_application

# <--- BƯỚC 2: THÊM CODE THÊM ĐƯỜNG DẪN DỰ ÁN VÀO PYTHON PATH
path_to_backend = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if path_to_backend not in sys.path:
    sys.path.insert(0, path_to_backend)
# ------------------------------------------------------------------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.Backend.settings')

application = get_wsgi_application()