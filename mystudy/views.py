import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string, get_template
from django.template import Context, Template, RequestContext
from django.core.context_processors import csrf


from mystudy.models import Topic, Category, Update, TopicResource
from mystudy.forms import TopicForm, CategoryForm, UpdatesForm, TopicResourceForm

from aresource.models import Resource, ResourceType
from people.models import Person

from people.decorators import owner_required

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
        return Topic.objects.filter(person=self.person).order_by('-last_viewed')
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserTopicListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['person'] = self.person
        return context


class TopicDetailView(DetailView):
    context_object_name = 'topic'
    template_name = 'mystudy/topic_detail.html'

    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        slug = self.kwargs.get('slug', None)
        try:
            obj = Topic.objects.get(person__user__username=person, slug=slug)
        except TopicDoesNotExist:
            raise Http404
        if self.request.user == obj.person.user:
            obj.last_viewed = datetime.datetime.now()
            obj.save()
        # Return the object
        return obj
        
    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['update_form'] = UpdatesForm()
        context['tr_form'] = TopicResourceForm()
        context['update_list'] = Update.objects.filter(topic=self.object).order_by('-added')
        context['tr_list'] = TopicResource.objects.select_related().filter(topic=self.object).order_by('-added')
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
    
    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        slug = self.kwargs.get('slug', None)
        try:
            obj = Topic.objects.get(person__user__username=person, slug=slug)
        except TopicDoesNotExist:
            raise Http404
        if not self.request.user == obj.person.user:
            raise Http404
        return obj
    
    
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
            
    
def tr_create_xhr(request, person, slug):
    if request.method == "POST":
        form = TopicResourceForm(request.POST)
        if form.is_valid():
            try:
                r = Resource.objects.get(url=form.cleaned_data['resource'])
            except Resource.DoesNotExist:
                r = Resource.objects.create(url=form.cleaned_data['resource'], rtype=form.cleaned_data['rtype'])
                r.save()
        obj = form.save(commit=False)
        obj.resource = r
        try:
            topic = Topic.objects.get(person__user=request.user, slug__iexact=slug)
        except Topic.DoesNotExist:
            return Http404
        obj.topic = topic        
        obj.save()
        html = render_to_string('includes/tr_inc.html',{"r":obj,"topic":topic})
        res = {'html':html}
        if request.is_ajax():
            return HttpResponse(simplejson.dumps(res), mimetype="application/json")
        else:
            return HttpResponseRedirect("../..")
    return Http404
    
    
def tr_edit_xhr(request, nid):
    if request.is_ajax():
        if request.method == "GET":
            tr = TopicResource.objects.get(id=nid)
            t = tr.resource.url
            data = {"resource":t}
            form = TopicResourceForm(instance=tr)
#            form.resource=str(tr.resource.url)
#            form.save(commit=False)
            c = {"form":form}
            c.update(csrf(request))
            formt = 'includes/gen_form_inc.html'
            html = render_to_string(formt, c)
            res = {"html":html}
            response = simplejson.dumps(res)
            return HttpResponse(response, mimetype='application/json')
        if request.method == "POST":
            tr = TopicResource.objects.get(id=nid)
            form = TopicResourceForm(request.POST, instance=tr)
            if form.is_valid():
                form = form.save()
                template = 'includes/tr_inc.html'
                html = render_to_string(template, {"r":form})
                res = {"html":html}
                response = simplejson.dumps(res)
                return HttpResponse(response, mimetype='application/json')
            else:
                return Http404
    return Http404
                
        
def update_create_xhr(request, person, slug):
    if request.method == "POST":
        form = UpdatesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
        else:
            return Http404
        try:
            t = Topic.objects.get(person__user=request.user, slug__iexact=slug)
        except Topic.DoesNotExist:
            return Http404
        form.topic = t
        form.save()
        if request.is_ajax():
            html = render_to_string('includes/update_inc.html',{"u":form,"topic":t})
            res = {"html":html}
            response = simplejson.dumps(res)
            return HttpResponse(response, mimetype='application/json')
        else:
            return HttpResponseRedirect('../..')
    return Http404
    
    
def update_edit_xhr(request, nid):
    if request.is_ajax():
        if request.method == "GET":
            note = Update.objects.get(id=nid)
            form = UpdatesForm(instance=note)
            c = {"form":form}
            c.update(csrf(request))
            formt = 'includes/gen_form_inc.html'
            html = render_to_string(formt, c)
            res = {"html":html}
            response = simplejson.dumps(res)
            return HttpResponse(response, mimetype='application/json')
        if request.method == "POST":
            note = Update.objects.get(id=nid)
            form = UpdatesForm(request.POST, instance=note)
            if form.is_valid():
                form = form.save()
                template = 'includes/update_inc.html'
                html = render_to_string(template, {"u":form})
                res = {"html":html}
                response = simplejson.dumps(res)
                return HttpResponse(response, mimetype='application/json')
            else:
                return Http404
    return Http404
    

class TopicResourcesDetailView(DetailView):
    context_object_name = 'topic_resource'
    template_name = 'mystudy/topicresources_detail.html'
    
#    def get_object(self, queryset=None)


class TopicResourceEditView(UpdateView):
    context_object_name = 'topicresource'
    model = TopicResource
    form_class = TopicResourceForm
    template_name = 'mystudy/topicresources_edit.html'
    success_url = '../../..'
    
    def get_initial(self):
        initial = super(TopicResourceEditView, self).get_initial()
        #TODO: proper auto-generation of code
        self.object = TopicResource.objects.get(id=self.object.id)
        r = self.object.resource.url
        initial.update({'resource': str(r)})
        return initial
        
    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        pk = self.kwargs.get('pk', None)
        try:
            obj = TopicResource.objects.get(id=pk)
        except TopicResource.DoesNotExist:
            raise Http404
        if not self.request.user == obj.topic.person.user:
            raise Http404
        return obj
        
        
    


class TopicResourcesListView(ListView):
    context_object_name = 'tr_list'
    template_name = 'mystudy/topicresources_list.html'
    
    def get_queryset(self):
        self.topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
        return TopicResource.objects.selected_related().filter(topic=self.topic)
        
    def get_context_data(self, **kwargs):
        context = super(TopicResourcesListView, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        return context
        
        
class TopicResourceDeleteView(DeleteView):
    context_object_name = 'topicresource'
    template_name = 'mystudy/topicresource_delete.html'
    model = TopicResource
    success_url = '../../..'
    
    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        pk = self.kwargs.get('pk', None)
        try:
            obj = TopicResource.objects.get(id=pk)
        except TopicResource.DoesNotExist:
            raise Http404
        if not self.request.user == obj.topic.person.user:
            raise Http404
        return obj
    

class UpdatesListView(ListView):
    
    context_object_name = 'update_list'
    template_name = 'mystudy/updates_list.html'
   
    def get_queryset(self):
        self.topic = get_object_or_404(Topic, slug=self.kwargs['slug'])
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
        topic = Topic.objects.get(person__user=request.user, slug__iexact=self.kwargs['slug'])
        if request.user != topic.person.user:
            return Http404
        self.object.topic = topic
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        
        
class UpdateEditView(UpdateView):
    context_object_name = 'update'
    model = Update
    form_class = UpdatesForm
    template_name = 'mystudy/updates_edit.html'
    success_url = '../../..'
    
    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        pk = self.kwargs.get('pk', None)
        try:
            obj = Update.objects.get(id=pk)
        except Update.DoesNotExist:
            raise Http404
        if not self.request.user == obj.topic.person.user:
            raise Http404
        return obj
    
    
class UpdateDeleteView(DeleteView):
    context_object_name = 'update'
    template_name = 'mystudy/update_delete.html'
    model = Update
    success_url = '../../..'
    
    def get_object(self, queryset=None):
        person = self.kwargs.get('person', None)
        pk = self.kwargs.get('pk', None)
        try:
            obj = Update.objects.get(id=pk)
        except Update.DoesNotExist:
            raise Http404
        if not self.request.user == obj.topic.person.user:
            raise Http404
        return obj
    

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
        context['topic_list'] = TaggedItem.objects.get_by_model(Topic, self.t)
        return context
        
        
class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        topic_list = Topic.objects.all().order_by('-created')[:7]
        resource_list = Resource.objects.all().order_by('-added')[:7]
        people_list = Person.objects.all().order_by('-user__date_joined')[:10]
        return {'topic_list': topic_list, 'resource_list': resource_list, 'person_list': people_list}
    


