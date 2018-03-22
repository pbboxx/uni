# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Program, Category,Location

from mptt.admin import MPTTModelAdmin


admin.site.register(Program)
admin.site.register(Location)
admin.site.register(Category) 