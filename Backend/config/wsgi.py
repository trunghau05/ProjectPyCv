"""
WSGI config for Backend project.
...
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Cấp đường dẫn: Thêm thư mục 'Backend' (chứa các app) vào sys.path
# 'Backend/Backend/wsgi.py' -> '..' -> 'Backend/' (thư mục gốc chứa các app)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.config.settings')

application = get_wsgi_application()