DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://10.5.0.1:8088', 'http://localhost:8088']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://10.5.0.1:8088'

APIS = {
    'authentication': 'http://10.5.0.1:8088',
    'base': 'http://10.5.0.1:8088',
    'booth': 'http://10.5.0.1:8088',
    'census': 'http://10.5.0.1:8088',
    'mixnet': 'http://10.5.0.1:8088',
    'postproc': 'http://10.5.0.1:8088',
    'store': 'http://10.5.0.1:8088',
    'visualizer': 'http://10.5.0.1:8088',
    'voting': 'http://10.5.0.1:8088',
}
