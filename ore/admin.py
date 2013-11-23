from django.contrib import admin
from ore.models import *
from mptt.admin import MPTTModelAdmin
from django.conf.urls import patterns, include, url
# Create your views here.



admin.site.register(Cliente)
admin.site.register(Cantiere)
admin.site.register(Dipendente)
admin.site.register(Attivita)

admin.site.register(Categoria_attivita,MPTTModelAdmin)

class slAdmin(admin.ModelAdmin):
    list_filter = ('dipendente', 'cantiere',)
    form = Scheda_lavoroForm

admin.site.register(Scheda_lavoro,slAdmin)
