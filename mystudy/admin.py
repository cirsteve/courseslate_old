from django.contrib import admin
from mystudy.models import Category, Topic, Update, TopicResource
from treebeard.admin import TreeAdmin

class StudyCatTreeAdmin(TreeAdmin):
	pass

admin.site.register(Category, StudyCatTreeAdmin)
admin.site.register(Topic)
admin.site.register(Update)
admin.site.register(TopicResource)