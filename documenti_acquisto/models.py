from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django import forms
from suit.widgets import SuitDateWidget
from django.contrib.admin import widgets

# Create your models here.

class Fornitore(models.Model):
    rag = models.TextField('Ragione Sociale', max_length=50)
    mail = models.EmailField('E-Mail', blank=True, null=True)
    telefono = models.IntegerField('Telefono principale', blank=True, null=True)
    indirizzo = models.TextField('Indirizzo', max_length=100, blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.rag)
    class Meta:
        verbose_name = "Fornitore"
        verbose_name_plural = "Fornitori"

class Fattura_acquisto(models.Model):
    data_emissione = models.DateField('Data di emissione')
    fornitore = models.ForeignKey(Fornitore, related_name='fornitore_fattura')
    data_scadenza = models.DateField('Data di scadenza')
    importo = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        verbose_name = 'Fattura di acquisto'
        verbose_name_plural = 'Fatture di acquisto'
    #def __unicode__(self):
    #    pass
    
class Fattura_acquistoForm(forms.ModelForm):
    #data = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Fattura_acquisto
        widgets = {
            'data_emissione': SuitDateWidget,
            'data_scadenza': SuitDateWidget,
        }