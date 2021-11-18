import os
from .settings import BASE_DIR

SECRET_KEY = 'aj3q*=5affgxtugm1h#03hdah)b#ukecr52tsncv)tfjj+gc@y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'm2m_relations',
        'USER': 'reguser',
        'PASSWORD': '321321',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}