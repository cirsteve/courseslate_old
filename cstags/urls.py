from django.conf.urls.defaults import *

from cstags.views import CSTagListView, CSTagDetailView

urlpatterns = patterns('',
    url(r'(?P<slug>[-\w]+)/$', CSTagDetailView.as_view(), name='cstag_detail'),
    url(r'^$', CSTagListView.as_view(), name='cstag_list'),
)