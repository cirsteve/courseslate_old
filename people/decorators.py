from django.utils.functional import wraps
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from mystudy.models import Topic, Update, TopicResource
from aresource.models import PersonalResource
"""

def owner_required(view, model):
    @wraps(view)
    def inner(request, *args, **kwargs):
        model = model
        if request.user.is_authenticated() == False:
            HttpResponseRedirect('/')
        if model == 'Topic':
            object = get_object_or_404(Topic, slug=kwargs['slug'])
            if request.user != object.person.user:
                return HttpResponseRedirect('/')
        if model == 'PersonalResource':
            object = get_object_or_404(model, id=kwargs['pk'])
            if request.user != object.person.user:
                return HttpResponseRedirect('/')
        else:
            object = get_object_or_404(model, id=kwargs['pk'])
            if request.user != object.topic.person.user:
                return HttpResponseRedirect('/')
        return view(request, *args, **kwargs)
        
    return inner
    
"""
"""
def owner_required(model):
    
    
    def _dec(view):
        def _inner(request, *args, **kwargs):
            if request.user.is_authenticated() == False:
                HttpResponseRedirect('/')
            model = kwargs['model']
            if model == 'Topic':
                object = get_object_or_404(Topic, slug=kwargs['slug'])
                if request.user != object.person.user:
                    return HttpResponseRedirect('/')
            if model == 'PersonalResource':
                object = get_object_or_404(model, id=kwargs['pk'])
                if request.user != object.person.user:
                    return HttpResponseRedirect('/')
            else:
                object = get_object_or_404(model, id=kwargs['pk'])
                if request.user != object.topic.person.user:
                    return HttpResponseRedirect('/')
            response = view.as_view(request, *args, **kwargs)
            return response
        
        return wraps(view)(_inner)
    return _dec
    
"""

def owner_required():
    
    
    def _dec(view):
        @wraps(view)
        def _inner(request, *args, **kwargs):
            if request.user.is_authenticated() == False:
                HttpResponseRedirect('/')

            if model == Topic:
                try:
                    object = Topic.objects.filter(person__user=request.user).get(slug=kwargs['slug'])
                except Topic.DoesNotExist:
                    return HttpResponseRedirect('/')
            if model == PersonalResource:
                try:
                    object = PersonalResource.objects.filter(person__user=request.user).get(id=kwargs['pk'])
                except PersonalResource.DoesNotExist:
                    return HttpResponseRedirect('/')
            else:
                object = get_object_or_404(model, id=kwargs['pk'])
                if request.user != object.topic.person.user:
                    return HttpResponseRedirect('/')
            response = view(request, *args, **kwargs)
            return response
        
        return _inner
    return _dec
