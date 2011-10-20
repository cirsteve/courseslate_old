from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from treebeard.mp_tree import MP_Node
from tagging.fields import TagField
#from people.models import Person

import tagging

class ResourceType(MP_Node):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, editable=False)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s' % self.name

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ResourceType, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return '/resources/type/%s' % self.slug

class Resource(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(unique=True)
    video = models.BooleanField()
    rtype = models.ForeignKey(ResourceType, verbose_name="Resource Type", blank=True, null=True)
    
    def __unicode__(self):
        return '%s' % self.url
    
    def get_absolute_url(self):
        return '/resources/%s' % self.id
        
        
class PersonalResource(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140, blank=True)
    note = models.TextField(blank=True)
    resource = models.ForeignKey('aresource.Resource')
    person = models.ForeignKey('people.Person')
    video = models.BooleanField()
    rtype = models.ForeignKey('aresource.ResourceType',verbose_name="Resource Type", blank=True, null=True)
    tag = TagField()
    
    def __unicode__(self):
        return self.resource
        
    def get_absolute_url(self):
        return '/people/user-resources/%s/%s' % (self.person.user, self.pk)
        
        


tagging.register(PersonalResource)