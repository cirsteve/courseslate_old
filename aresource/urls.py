from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from aresource.views import ResourceListView, ResourceDetailView, ResourceCreateView
from aresource.views import ResourceTypeDetailView, ResourceTypeListView, ResourceTypeCreateView
from aresource.views import ResourceTagListView, ResourceTagDetailView
from aresource.views import PersonalResourceCreateView, PersonalResourceDetailView, PersonalResourceListView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'type/$', ResourceTypeListView.as_view(), name='resource_type_list'),
    url(r'type/(?P<slug>[-\w]+)/$', ResourceTypeDetailView.as_view(), name='resource_type_detail'),
    url(r'tags/$', ResourceTagListView.as_view(), name='resource_tags_list'),
    url(r'tags/(?P<name>[-\w]+)/$', ResourceTagDetailView.as_view(), name='resource_tags_detail'),
#    url(r'create/$', login_required(ResourceCreateView.as_view())),
    url(r'(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^$', ResourceListView.as_view(), name='resource_list'),
)