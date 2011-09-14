from django.conf.urls.defaults import patterns, include, url
from mystudy.views import TopicListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^resources/', include('aresource.urls')),
    url(r'^topics/', include('mystudy.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^messages/', include('django_messages.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^accounts/', include('myreg.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TopicListView.as_view()),
)
