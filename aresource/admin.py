from django.contrib import admin
from aresource.models import ResourceType, Resource, PersonalResource
from treebeard.admin import TreeAdmin

class ResourceTypeTreeAdmin(TreeAdmin):
    pass

admin.site.register(ResourceType, ResourceTypeTreeAdmin)
admin.site.register(Resource)
admin.site.register(PersonalResource)
