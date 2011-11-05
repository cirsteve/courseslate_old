from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from aresource.views import ResourceListView, ResourceDetailView, ResourceCreateView
from aresource.views import ResourceTypeDetailView, ResourceTypeListView, ResourceTypeCreateView
from aresource.views import ResourceTagListView, ResourceTagDetailView
from aresource.views import PersonalResourceCreateView, PersonalResourceDetailView, PersonalResourceListView
from aresource.views import resource_set_json, get_tags_json
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'get-json/resource-set/(?P<restype>[-\w]+)/(?P<resset>[-\w]+)/$', resource_set_json, name='resource_set_json'),
    url(r'get-json/tag-set/for-user/', login_required(get_tags_json), name='get_tags_json'),
    url(r'type/$', ResourceTypeListView.as_view(), name='resource_type_list'),
    url(r'type/(?P<slug>[-\w]+)/$', ResourceTypeDetailView.as_view(), name='resource_type_detail'),
    url(r'tags/$', ResourceTagListView.as_view(), name='resource_tags_list'),
    url(r'tags/(?P<name>[-\w]+)/$', ResourceTagDetailView.as_view(), name='resource_tags_detail'),
#    url(r'create/$', login_required(ResourceCreateView.as_view())),
    url(r'(?P<pk>\d+)/$', ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^$', ResourceListView.as_view(), name='resource_list'),
)