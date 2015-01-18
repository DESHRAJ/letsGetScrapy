from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
# import settings
# import allot.urls
from scrapy.urls import * 
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'scrapy.views.home', name='home'),
    url(r'collages', 'scrapy.views.collages', name='collages'),
    url(r'greeting', 'scrapy.views.greeting', name='greeting'),
    url(r'photograph', 'scrapy.views.photograph', name='photograph'),
    url(r'scrapbook', 'scrapy.views.scrapbook', name='scrapbook'),
    url(r'finalstep', 'scrapy.views.finalstep', name='finalstep'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)