from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from treebeard.mp_tree import MP_Node
from tagging.fields import TagField

#from people.models import Person
import tagging
# Create your models here.

class Category(MP_Node):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(blank=True)

    node_order_by = ['name']

    def __unicode__(self):
        return '%s' % self.name

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return '/topics/category/%s' % self.slug

class Topic(models.Model):
    STATUS_CHOICES = (
        (0, 'Ongoing'),
        (1, 'Completed'),
    )
    person = models.ForeignKey('people.Person')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    tag = TagField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    last_viewed = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    dmod_count = models.IntegerField(default=0)
    resources = models.ManyToManyField('aresource.Resource',
        through='mystudy.TopicResource', null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        else:
            ot = Topic.objects.get(id=self.id)
            if ot.deadline != self.deadline:
                self.dmod_count = ot.dmod_count + 1
        super(Topic, self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return '/topics/%s' % self.slug
        
    class Meta:
        unique_together = (("person", "title"),("person", "slug"))


class Update(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField()
    topic = models.ForeignKey(Topic)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return '%s' % self.pk
        
    def get_absolute_url(self):
        return '/topics/update/%s' % self.pk

class TopicResource(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=140, blank=True)
    note = models.TextField(blank=True)
    resource = models.ForeignKey('aresource.Resource')
    rtype = models.ForeignKey('aresource.ResourceType', verbose_name="Resource Type", blank=True, null=True)
    topic = models.ForeignKey('mystudy.Topic')

    def __unicode__(self):
        return '%s on %s' % (self.resource, self.topic)

    def get_absolute_url(self):
        return '/topics/%s/%s/%s' % (self.topic.slug, self.resource.id,
            self.id)