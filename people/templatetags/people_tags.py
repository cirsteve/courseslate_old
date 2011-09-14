from django import template

from mystudy.models import Topic

register = template.Library()

class RecentlyViewedNode(template.Node):
    def __init__(self, username):
        self.username = username
    def render(self, context):
        context['recently_viewed_t'] = Topic.objects.filter(person__user__username__iexact=self.username).order_by('last_viewed')
        recently_viewed_t = Topic.objects.filter(person__user__username__iexact=self.username).order_by('last_viewed')
        return context['recently_viewed_t']


def recently_viewed(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, username = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires one argument" % token.contents.split()[0])
    return RecentlyViewedNode(username)
    
register.tag('recently_viewed_topics', recently_viewed)