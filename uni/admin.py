# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources

from .models import Program, Category,Location
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin



class ProgramResource(resources.ModelResource):
    """
    class use to import and export ressource
    """

    class Meta:
        model = Program
        skip_unchanged = True
        report_skipped = False



class ProgramAdmin(ImportExportModelAdmin):
    """
    give acces through admin interface to ProgramRessource
    """
    resource_class = ProgramResource
admin.site.register(Program,ProgramAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)
admin.site.register(Category)

