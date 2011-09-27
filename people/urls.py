from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from people.decorators import owner_required

from people.views import PeopleListView, PeopleDetailView, PeopleEditView, AccountEditView
from aresource.views import PersonalResourceCreateView, PersonalResourceEditView, PersonalResourceDetailView, PersonalResourceListView
from aresource.models import PersonalResource

urlpatterns = patterns('',
    url(r'user-resources/edit/(?P<pk>[-\d]+)/$', PersonalResourceEditView.as_view(), name='personalresource_edit'),
    url(r'user-resources/add/$', login_required(PersonalResourceCreateView.as_view()), name='personalresource_create'),
    url(r'user-resources/(?P<person>[-\w]+)/$', PersonalResourceListView.as_view(), name='personalresource_list'),
    url(r'user-resources/(?P<person>[-\w]+)/(?P<pk>\d+)/$', PersonalResourceDetailView.as_view(), name='personalresource_detail'),
    url(r'edit-profile/$', login_required(PeopleEditView.as_view()), name='people_edit'),
    url(r'edit-account/$', login_required(AccountEditView.as_view()), name='account_edit'),
    url(r'(?P<user>[-\w]+)/$', PeopleDetailView.as_view(), name='people_detail'),
    url(r'^$', PeopleListView.as_view(), name='people_list'),
)