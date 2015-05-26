from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^about/', 'signups.views.get_started', name='get_started'),
    url(r'^revenue_model/', 'signups.views.revenue_model', name='revenue_model'),
    url(r'^contact/', 'signups.views.contact', name='contact'),
    url(r'^signup_page/', 'signups.views.signup_page', name='signup_page'),
        
    # English
    #url(r'^en/', 'signups.views.en', name='en'),

    # Korean
    
    # Chinese
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)