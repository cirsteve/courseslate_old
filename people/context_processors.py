from django.contrib.auth.models import User

from mystudy.models import Topic
from aresource.models import PersonalResource

def resource_options(request):
    if request.user.is_authenticated():
        user = User.objects.get(user=request.user)
        options = []
        pr = PersonalResource.objects.filter(person__user__username=user)
        for r in pr:
            for t in r.tags:
                if t.name in options:
                    pass
                else:
                    option = 'Tag-%s' % t.name
                    options.append(option)
                
        topics = Topic.objects.filter(person__user__username=user)
        for t in topics:
            option = 'Course-%s' % t.title
            options.append(option)
        return {'resource_opt':options}
    else:
        pass