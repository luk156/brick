from django.contrib import admin
from documenti_acquisto.models import *
from mptt.admin import MPTTModelAdmin
from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _
import datetime as dt
from import_export.admin import ImportExportModelAdmin
# Create your views here.

admin.site.register(Fornitore)


class ScadenzeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('In scadenza')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'data_scadenza'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('scadenze', _('in scadenza')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        oggi = dt.date.today()
        if self.value() == 'scadenze':
            return queryset.filter(data_scadenza__month=oggi.month)

class Fattura_acquistoAdmin(ImportExportModelAdmin):
    date_hierarchy = 'data_scadenza'
    list_display = ('fornitore', 'data_scadenza', 'importo')
    #list_filter = (ScadenzeListFilter,)
    ordering = ['-data_scadenza']
    def suit_row_attributes(self, obj, request):
        oggi = dt.date.today()
        if obj.data_scadenza.month==oggi.month:
         return {'class': 'error'}

admin.site.register(Fattura_acquisto, Fattura_acquistoAdmin)
