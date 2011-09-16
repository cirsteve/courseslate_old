# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from aresource.models import Resource, ResourceType, PersonalResource
from aresource.forms import ResourceForm, PersonalResourceForm
from mystudy.models import TopicResource, Topic
from people.models import Person

from tagging.models import Tag, TaggedItem

class ResourceListView(ListView):
	context_object_name = 'resource_list'
	model = Resource
	template_name = 'aresource/resource_list.html'


class ResourceDetailView(DetailView):
    context_object_name = 'resource'
    model = Resource
    template_name = 'aresource/resource_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView, self).get_context_data(**kwargs)
        context['tr_list'] = TopicResource.objects.filter(resource=self.object)
        context['pr_list'] = PersonalResource.objects.filter(resource=self.object)
        return context


class ResourceTypeListView(ListView):
	context_object_name = 'resourcetype_list'
	model = ResourceType
	template_name = 'aresource/resourcetype_list.html'


class ResourceTypeDetailView(DetailView):
    context_object_name = 'resourcetype'
    model = ResourceType
    template_name = 'aresource/resourcetype_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ResourceTypeDetailView, self).get_context_data(**kwargs)
        context['resource_list'] = self.object.resource_set.all()
        return context


class ResourceTypeCreateView(CreateView):
	model = ResourceType
	template_name = 'aresource/resourcetype_create.html'


class ResourceCreateView(CreateView):
    form_class = ResourceForm
    model = Resource
    template_name = 'aresource/resource_create.html'
    
    
class PersonalResourceDetailView(DetailView):
    context_object_name = 'resource'
    model = PersonalResource
    template_name = 'aresource/personalresource_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonalResourceDetailView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['user'] = Person.objects.get(user__username=self.kwargs['person'])
        return context
    
    
class PersonalResourceCreateView(CreateView):
    context_object_name = 'resource'
    template_name = 'aresource/personalresource_create.html'
    form_class = PersonalResourceForm
    success_url = '../..'
    
    def form_valid(self, form):
        try:
            r = Resource.objects.get(url=form.cleaned_data['resource'])
            r.save()
        except Resource.DoesNotExist:
            u = get_object_or_404(Person, user=self.request.user)
            r = Resource.objects.create(url=form.cleaned_data['resource'])
            r.save()
        self.object = form.save(commit=False)
        self.object.person = get_object_or_404(Person, user=self.request.user)
        self.object.resource = r
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        

class PersonalResourceEditView(UpdateView):
    context_object_name = 'resource'
    template_name = 'aresource/personalresource_edit.html'
    form_class = PersonalResourceForm
    model = PersonalResource
        
        
    def get_initial(self):
        initial = super(PersonalResourceEditView, self).get_initial()
        #TODO: proper auto-generation of code
        res = PersonalResource.objects.get(id=self.object.id)
        r = res.resource.url
        initial.update({'resource': str(r)})
        return initial
        
        
class PersonalResourceListView(ListView):
    context_object_name = 'pr_list'
    model = PersonalResource
    template_name = 'aresource/personalresource_list.html'
    
    def get_queryset(self, **kwargs):
        self.person = get_object_or_404(Person, user__username__iexact=self.kwargs['person'])
        return PersonalResource.objects.filter(person=self.person)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonalResourceListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['person'] = self.person
        return context
        
     
class ResourceTagDetailView(DetailView):
    context_object_name = 'tag'
    model = Tag
    template_name = 'aresource/resource_tag_detail.html'
    
    def get_object(self):
        self.t = get_object_or_404(Tag, name=self.kwargs['name'])
        return self.t
        
    def get_context_data(self, **kwargs):
        context = super(ResourceTagDetailView, self).get_context_data(**kwargs)
        context['pr_list'] = TaggedItem.objects.get_by_model(PersonalResource, self.t)
        topics = TaggedItem.objects.get_by_model(Topic, self.t)
        context['tr_list'] = []
        for r in topics:
            for tr in r.topicresource_set.all():
                context['tr_list'].append(tr)
        return context
        
        
class ResourceTagListView(ListView):
    context_object_name = 'tag_list'
    model = Tag
    template_name = 'aresource/resource_tag_list.html'