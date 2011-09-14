from django.forms import ModelForm, Textarea, CharField, URLField, TextInput
from treebeard.forms import MoveNodeForm
from mystudy.models import Topic, Category, Update, TopicResource


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'description', 'category', 'tag', 'deadline', 'status')
        
        
class CategoryForm(MoveNodeForm):
    class Meta:
        model = Category
        fields = ('name', 'description')


class UpdatesForm(ModelForm):
    class Meta:
        model = Update
        fields = ('title', 'comment')


class TopicResourceForm(ModelForm):
    resource = URLField(label='Resource URL', widget=TextInput(attrs={'size':'70'}))
    class Meta:
        model = TopicResource
        fields = ('title', 'rtype', 'note')