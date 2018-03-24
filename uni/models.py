# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Program(models.Model):
  name = models.CharField(max_length=120)
  courses = models.CharField(max_length=220)
  university = models.CharField(max_length=220)
  level = models.CharField(max_length=220)
  link =  models.CharField(max_length=220)
  ranking  =  models.CharField(max_length=220)
  category = TreeForeignKey('Category',null=True,blank=True, on_delete=models.CASCADE)
  location=  TreeForeignKey('Location',null=True,blank=True, on_delete=models.CASCADE)
  content = models.TextField('Content')
  slug = models.SlugField()

  def __str__(self):
    return self.name




class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name



class Location(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'locations'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name