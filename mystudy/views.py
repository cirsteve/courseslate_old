import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from mystudy.models import Topic, Category, Update, TopicResource
from mystudy.forms import TopicForm, CategoryForm, UpdatesForm, TopicResourceForm

from aresource.models import Resource, ResourceType
from people.models import Person

from tagging.models import Tag, TaggedItem

class TopicListView(ListView):

    context_object_name = 'topic_list'
    queryset = Topic.objects.all()
    template_name = 'mystudy/topic_list.html'


class UserTopicListView(ListView):
    context_object_name = 'topic_list'
    template_name = 'mystudy/user_topic_list.html'
    
    def get_queryset(self):
        self.person = get_object_or_404(Person, user__username__iexact=self.kwargs['person'])
        return Topic.objects.filter(person=self.person)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserTopicListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['person'] = Person.objects.get(user__username__iexact=self.kwargs['person'])
        return context


class TopicDetailView(DetailView):
    context_object_name = 'topic'
    queryset = Topic.objects.all()
    template_name = 'mystudy/topic_detail.html'

    def get_object(self):
        # Call the superclass
        object = super(TopicDetailView, self).get_object()
        # Record the last accessed date
        if self.request.user == object.person.user:
            object.last_viewed = datetime.datetime.now()
            object.save()
        # Return the object
        return object
        
    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['update_form'] = UpdatesForm()
        context['tr_form'] = TopicResourceForm()
        context['update_list'] = Update.objects.filter(topic=self.object).order_by('-added')
        context['tr_list'] = TopicResource.objects.filter(topic=self.object)
        return context
    
class TopicCreateView(CreateView):
    form_class = TopicForm
    model = Topic
    template_name = 'mystudy/topic_create.html'
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.person = get_object_or_404(Person, user=self.request.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
        
class TopicEditView(UpdateView):
    context_object_name = 'topic'
    model = Topic
    form_class = TopicForm
    template_name = 'mystudy/topic_edit.html'
    
#    def dispatch(request, **kwargs):
    
class TopicResourcesCreateView(CreateView):
    form_class = TopicResourceForm
    model = TopicResource
    template_name = 'mystudy/topicresources_create.html'
    success_url = '../..'

    def form_valid(self, form):
        try:
            r = Resource.objects.get(url=form.cleaned_data['resource'])
        except Resource.DoesNotExist:
            r = Resource.objects.create(url=form.cleaned_data['resource'], rtype=form.cleaned_data['rtype'])
            r.save()
        self.object = form.save(commit=False)
        self.object.resource = r
        topic = Topic.objects.get(slug__iexact=self.kwargs['slug'])
        self.object.topic = topic
        self.object.save()
        return super(TopicResourcesCreateView, self).form_valid(form) 

class TopicResourcesDetailView(DetailView):
	context_object_name = 'topic_resource'
	queryset = Topic.objects.all()
	template_name = 'mystudy/topicresources_detail.html'
	

class TopicResourceEditView(UpdateView):
    context_object_name = 'topicresource'
    model = TopicResource
    form_class = TopicResourceForm
    template_name = 'mystudy/topicresources_edit.html'
    success_url = '../../..'
    
    def get_initial(self):
        initial = super(TopicResourceEditView, self).get_initial()
        #TODO: proper auto-generation of code
        res = TopicResource.objects.get(id=self.object.id)
        r = res.resource.url
        initial.update({'resource': str(r)})
        return initial


class TopicResourcesListView(ListView):
    context_object_name = 'tr_list'
    template_name = 'mystudy/topicresources_list.html'
    
    def get_queryset(self):
        self.topic = get_object_or_404(Topic, slug=self.kwargs['topic'])
        return TopicResource.objects.filter(topic=self.topic)
        
    def get_context_data(self, **kwargs):
        context = super(TopicResourcesListView, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        return context
        
        
class TopicResourceDeleteView(DeleteView):
    context_object_name = 'topicresource'
    template_name = 'mystudy/topicresource_delete.html'
    model = TopicResource
    success_url = '../..'
    
	
class UpdatesListView(ListView):
    
    context_object_name = 'update_list'
    template_name = 'mystudy/updates_list.html'
   
    def get_queryset(self):
        self.topic = get_object_or_404(Topic, slug=self.kwargs['topic'])
        return Update.objects.filter(topic=self.topic)
        
    def get_context_data(self, **kwargs):
        context = super(UpdatesListView, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        return context
        
class UpatesDetailView(DetailView):
	context_object_name = 'update'
	queryset = Update.objects.all()
	template_name = 'mystudy/updates_detail.html'
	
class UpdatesCreateView(CreateView):
    form_class = UpdatesForm
    model = Update
    template_name = 'mystudy/updates_create.html'
    success_url = '../..'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        topic = Topic.objects.get(slug__iexact=self.kwargs['slug'])
        self.object.topic = topic
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
        
class UpdateEditView(UpdateView):
    context_object_name = 'update'
    model = Update
    form_class = UpdatesForm
    template_name = 'mystudy/updates_edit.html'
    success_url = '../../..'
    
    
class UpdateDeleteView(DeleteView):
    context_object_name = 'update'
    template_name = 'mystudy/update_delete.html'
    model = Update
    success_url = '../..'
    

class CategoryDetailView(DetailView):
    context_object_name = 'category'
    queryset = Category.objects.all()
    template_name = 'mystudy/category_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['topic_list'] = self.object.topic_set.all()
        return context


class CategoryListView(ListView):
	context_object_name = 'category_list'
	queryset = Category.objects.all()
	template_name = 'mystudy/category_list.html'
	
	
class  CategoryCreateView(CreateView):
	form_class = CategoryForm
	model = Category
	template_name = 'mystudy/category_create.html'
	
	
class TopicTagsListView(ListView):
    context_object_name = 'tag_list'
#    queryset = Tag.objects.get_for_object(Topic)
    template_name = 'mystudy/topic_tag_list.html'
   
    def get_queryset(self):
        return Tag.objects.usage_for_model(Topic, counts=True)
        
        
class TopicTagsDetailView(DetailView):
    context_object_name = 'tag'
    model = Tag
    template_name = 'mystudy/topic_tag_detail.html'
    queryset = Tag.objects.all()
    
    def get_object(self):
        self.t = get_object_or_404(Tag, name=self.kwargs['slug'])
        return self.t
    
    def get_context_data(self, **kwargs):
        context = super(TopicTagsDetailView, self).get_context_data(**kwargs)
        context['tag_list'] = TaggedItem.objects.get_by_model(Topic, self.t)
        return context

