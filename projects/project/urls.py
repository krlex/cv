from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'resume.views.home', name='home'),
    url(r'^resume/', include('resume.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
