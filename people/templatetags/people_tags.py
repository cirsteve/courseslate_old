from django import template
from django.contrib.auth.models import User

from mystudy.models import Topic
from aresource.models import PersonalResource

register = template.Library()
    
@register.inclusion_tag('includes/topic_list_inc.html')    
def person_topics(user):
    t = Topic.objects.filter(person__user__username__iexact=user).order_by('-last_viewed')[:4]
    return {"topic_list": t}
    
    
@register.inclusion_tag('includes/pr_list_inc.html')    
def person_resources(user):
    t = PersonalResource.objects.filter(person__user__username__iexact=user).order_by('-added')[:4]
    return {"pr_list": t}
    
    
@register.inclusion_tag('includes/topic_list_inc.html')    
def all_topics():
    t = Topic.objects.all().order_by('-created')[:4]
    return {"topic_list": t}
    
    
@register.inclusion_tag('includes/pr_list_inc.html')    
def all_resources():
    t = PersonalResource.objects.all().order_by('-added')[:4]
    return {"pr_list": t}
    

@register.inclusion_tag('includes/resource_options_inc.html')
def resource_options(user):
    user = User.objects.get(username=user)
    options = []
    options.append('Recent | 5')
    pr = PersonalResource.objects.filter(person__user__username=user)
    for r in pr:
        for t in r.tags:
            if t.name in options:
                pass
            else:
                option = 'Tag | %s' % t.name
                options.append(option)
                
    topics = Topic.objects.filter(person__user__username=user)
    for t in topics: 
        option = 'Course | %s' % t.title
        options.append(option)
    return {'resource_opt':options}


@register.filter
def sliceit(string, length):
    if length > len(string):
        return string
    else:
        l = length - 3
        s = string[:l] + '...'
        return s
