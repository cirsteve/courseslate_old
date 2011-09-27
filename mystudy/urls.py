from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from mystudy.views import UserTopicListView, TopicListView, TopicDetailView, TopicCreateView, TopicEditView
from mystudy.views import TopicResourcesCreateView, TopicResourcesListView, TopicResourceEditView, TopicResourceDeleteView, tr_create_xhr
from mystudy.views import UpdatesListView, UpdatesCreateView, UpdateEditView, UpdateDeleteView, update_create_xhr
from mystudy.views import CategoryCreateView, CategoryDetailView, CategoryListView
from mystudy.views import TopicTagsListView, TopicTagsDetailView
from mystudy.models import Topic, Update, TopicResource

from people.decorators import owner_required

urlpatterns = patterns('',
    url(r'category/$', CategoryListView.as_view(), name='topic_category_list'),
    url(r'category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='topic_category_detail'),
    url(r'create/$', login_required(TopicCreateView.as_view()), name='topic_create'),
    url(r'tags-cs/(?P<slug>[-\w]+)/$', TopicTagsDetailView.as_view(), name='topic_tags_detail'),
    url(r'tags-cs/$', TopicTagsListView.as_view(), name='topic_tags_list'),
    url(r'user/(?P<person>[-\w]+)/$', UserTopicListView.as_view(), name='user_topic_list'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/edit/$', TopicEditView.as_view(), name='topic_edit'),    
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/$', TopicDetailView.as_view(), name='topic_detail'),    
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/resources/$', TopicResourcesListView.as_view(), name='topic_resources'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/updates/$', UpdatesListView.as_view(), name='topic_updates'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/updates/add/$', login_required(update_create_xhr), name='topic_update_create'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/topic-resource/add/$', login_required(tr_create_xhr), name='topic_resource_create'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/updates/edit/(?P<pk>\d+)/$', UpdateEditView.as_view(), name='topic_update_edit'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/topic-resource/edit/(?P<pk>\d+)/$', TopicResourceEditView.as_view(), name='topic_resource_edit'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/updates/delete/(?P<pk>\d+)/$', UpdateDeleteView.as_view(), name='topic_update_delete'),
    url(r'user/(?P<person>[-\w]+)/(?P<slug>[-\w]+)/topic-resource/delete/(?P<pk>\d+)/$', TopicResourceDeleteView.as_view(), name='topic_resource_delete'),    
    url(r'^$', TopicListView.as_view(), name='topic_list'),
)