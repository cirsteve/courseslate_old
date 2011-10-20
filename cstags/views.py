from django.views.generic import ListView, DetailView

from tagging.models import Tag


class CSTagListView(ListView):
    context_object_name = 'tag_list'
    template_name = 'cstags/tag_list.html'
    model = Tag
    slug_field = 'name'
    
    def get_queryset(self):
        self.q = Tag.objects.all()
        return self.q
    
    
    
class CSTagDetailView(DetailView):
    context_object_name = 'tag'
    template_name = 'cstags/tag_detail.html'
    model = Tag
    slug_field = 'name'
    
