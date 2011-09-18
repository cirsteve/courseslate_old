from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from mystudy.views import UserTopicListView, TopicListView, TopicDetailView, TopicCreateView, TopicEditView
from mystudy.views import TopicResourcesCreateView, TopicResourcesListView, TopicResourceEditView, TopicResourceDeleteView
from mystudy.views import UpdatesListView, UpdatesCreateView, UpdateEditView, UpdateDeleteView
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
    url(r'(?P<topic>[-\w]+)/resources/$', TopicResourcesListView.as_view(), name='topic_resources'),
    url(r'(?P<topic>[-\w]+)/updates/$', UpdatesListView.as_view(), name='topic_updates'),
    url(r'(?P<slug>[-\w]+)/updates/add/$', login_required(UpdatesCreateView.as_view()), name='topic_update_create'),
    url(r'(?P<slug>[-\w]+)/topic-resource/add/$', login_required(TopicResourcesCreateView.as_view()), name='topic_resource_create'),
    url(r'(?P<slug>[-\w]+)/updates/edit/(?P<pk>\d+)/$', owner_required(UpdateEditView.as_view(), Update), name='topic_update_edit'),
    url(r'(?P<slug>[-\w]+)/topic-resource/edit/(?P<pk>\d+)/$', owner_required(TopicResourceEditView.as_view(), TopicResource), name='topic_resource_edit'),
    url(r'(?P<slug>[-\w]+)/updates/delete/(?P<pk>\d+)/$', owner_required(UpdateDeleteView.as_view(), Update), name='topic_update_delete'),
    url(r'(?P<slug>[-\w]+)/topic-resource/delete/(?P<pk>\d+)/$', owner_required(TopicResourceDeleteView.as_view(), TopicResource), name='topic_resource_delete'),    
    url(r'(?P<slug>[-\w]+)/edit/$', owner_required(TopicEditView.as_view(), Topic), name='topic_edit'),    
    url(r'(?P<slug>[-\w]+)/$', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^$', TopicListView.as_view(), name='topic_list'),
)