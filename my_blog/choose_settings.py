# choose settings between Developement and Deploy
import os
import platform

node = platform.node()
# dev_machines = ('RAINBOWSTONE')
dev_machines = ('GUOY-PC')

if node in dev_machines:
    # folder My_Blog
    My_Blog = os.path.dirname(os.path.dirname(__file__))
    # My_Blog = os.path.dirname(__file__)
    # project dir, contains static and media folder under DEV environment
    PROJECT_DIR = os.path.dirname(My_Blog)
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'myblog',
            'USER': 'admin',
            'PASSWORD': 'PwdMy0blog@dmin',
            'HOST': 'localhost',
            'PORT': 3306, 
        }
    }
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
    TEMPLATE_DIRS = [os.path.join(My_Blog, 'templates')]
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'myblog',
            'USER': 'admin',
            'PASSWORD': 'PwdMy0blog@dmin',
            'HOST': 'localhost',
            'PORT': 3306,
        }
    }
    PROJECT_DIR = '/blog/My_Blog/'
    # MEDIA_ROOT = '/blog/media/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
    # STATIC_ROOT = '/blog/static/'
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        ('css3two_blog', os.path.join(STATIC_ROOT, 'css3two_blog')),
        ('admin', os.path.join(STATIC_ROOT, 'admin')),
    ]

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '*',
        #        'www.rainbowstone.com',
    ]

    # cache entire site
#    MIDDLEWARE_CLASSES_ADDITION_FIRST = (
#        'django.middleware.cache.UpdateCacheMiddleware',
#    )

#    MIDDLEWARE_CLASSES_ADDITION_LAST = (
#        'django.middleware.cache.FetchFromCacheMiddleware',
#    )

#    CACHES = {
#        'default': {
#            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#            'LOCATION': '127.0.0.1:11211',
#        }
#    }
