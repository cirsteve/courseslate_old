from django import template

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

@register.filter
def sliceit(string, length):
    if length > len(string):
        return string
    else:
        l = length - 3
        s = string[:l] + '...'
        return s
