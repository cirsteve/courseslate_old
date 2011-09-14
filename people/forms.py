from django.forms import ModelForm, URLField, ModelChoiceField

from django.contrib.auth.models import User

from people.models import Person
from mystudy.models import Topic


class PeopleEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        #self.request = kwargs.pop('request', None)
        super(PeopleEditForm, self).__init__(*args, **kwargs)
        self.fields['primary_topic'] = ModelChoiceField(queryset=Topic.objects.filter(person__user=kwargs['initial']['user']),
        empty_label="Choose A Topic", required=False)
    class Meta:
        model = Person
        
        
class AccountEditForm(ModelForm):
    class Meta:
        model = User
        fields= ('username','first_name','last_name','email')