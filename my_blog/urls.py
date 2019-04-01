from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from css3two_blog import views as cv
from my_blog import views as mv

admin.autodiscover()

urlpatterns = [
                  # '',

                  # css3two_blog
                  url(r'^(?P<page>\d*)/$', cv.home),
                  url(r'^$', cv.home),
                  url(r'^blog/', include('css3two_blog.urls')),

                  # admin
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^referral/', mv.referral),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, name='media')

if not settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
        # url(r'^meidia/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    ]

handler404 = 'my_blog.views.handler404'
