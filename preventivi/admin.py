from django.contrib import admin
from preventivi.models import *
from mptt.admin import MPTTModelAdmin
from django.conf.urls import patterns, include, url
from import_export.admin import ImportExportModelAdmin
# Create your views here.

class DimensioneInline(admin.TabularInline):
    model = dimensione

class AttivitaInline(admin.TabularInline):
    model = preventivo_attivita

class PreventivoAdmin(ImportExportModelAdmin):
    date_hierarchy = 'data'
    list_display = ('cliente', 'data', 'totale')
    inlines = [
        AttivitaInline,
    ]
    ordering = ['-data']

admin.site.register(Preventivo, PreventivoAdmin)