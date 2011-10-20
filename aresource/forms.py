from django.forms import ModelForm, URLField, TextInput
from aresource.models import Resource, PersonalResource


class PersonalResourceForm(ModelForm):
    resource = URLField(label='Resource URL', widget=TextInput(attrs={'size':'70'}))
    class Meta:
        model = PersonalResource
        fields = ('title', 'note', 'video', 'rtype', 'tag')
        
        
class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        
        
