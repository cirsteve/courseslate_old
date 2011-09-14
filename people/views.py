from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from people.models import Person
from people.forms import PeopleEditForm, AccountEditForm

from mystudy.models import Topic
from aresource.models import PersonalResource

class PeopleListView(ListView):
    model = Person
    context_object_name = 'person_list'
    template_name = 'people/person_list.html'
    
    
class PeopleDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'people/person_detail.html'
    
    def get(self, request, **kwargs):
        # lookup Guide Id in your database and assign it object
        self.object = Person.objects.get(user__username__iexact=kwargs.get('user'))
        # add object to your context_data, so that you can access via your template
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
        
    def get_context_data(self, **kwargs):
        context = super(PeopleDetailView, self).get_context_data(**kwargs)
        context['topic_list'] = Topic.objects.filter(person=self.object)
        context['pr_list'] = PersonalResource.objects.filter(person=self.object)
        return context
        

class PeopleEditView(UpdateView):
    form_class = PeopleEditForm
    template_name = 'people/people_edit.html'
    #success_url = "/people/%(user.username)s/"
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(PeopleEditView, self).get_form_kwargs(**kwargs)
        kwargs['initial']['user'] = self.request.user
        return kwargs
    
    def get_object(self, queryset=None):
        obj = Person.objects.get(user=self.request.user)
        return obj
        
    
 
class AccountEditView(UpdateView):
    form_class = AccountEditForm
    template_name = 'people/account_edit.html'
    success_url = "/people/%(username)s/"
    
    def get_object(self, queryset=None):
        obj = User.objects.get(id=self.request.user.id)
        return obj