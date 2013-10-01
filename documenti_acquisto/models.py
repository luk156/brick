from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django import forms
from suit.widgets import SuitDateWidget
from django.contrib.admin import widgets
from ore.models import *

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

class Articolo(models.Model):
    descrizione = models.TextField('Descrizione', max_length=50)
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
    def __unicode__(self):
        return u'%s' % (self.descrizione)


class Documento_acquisto(models.Model):
    data_emissione = models.DateField('Data di emissione')
    fornitore = models.ForeignKey(Fornitore, related_name='fornitore_ddt')    
    class Meta:
        abstract = False
    def importo(self):
        i = 0
        for b in self.documento_bene.all():
            i = i + b.importo()
        return i


class Bene(models.Model):
    articolo = models.ForeignKey(Articolo, related_name='articolo_bene')
    quantita = models.DecimalField('Quantita', max_digits=8, decimal_places=2)
    prezzo_unitario = models.DecimalField('Prezzo unitario', max_digits=8, decimal_places=2)
    documento = models.ForeignKey('Documento_acquisto', related_name='documento_bene')
    cantiere = models.ForeignKey(Cantiere, related_name='cantiere_bene')
    class Meta:
        verbose_name = "Bene"
        verbose_name_plural = "Beni"
    def importo(self):
        return self.quantita * self.prezzo_unitario
    def __unicode__(self):
        return u'%s x %s' % (self.articolo,self.quantita)


class Documento_trasporto(Documento_acquisto):
    convertito = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Documento di trasporto'
        verbose_name_plural = 'Documenti di trasporto'
    def __unicode__(self):
        return u'%s (%s)' % (self.fornitore,self.data_emissione)


class Documento_trasportoForm(forms.ModelForm):
    #data = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Documento_trasporto
        exclude = ['convertito']
        widgets = {
            'data_emissione': SuitDateWidget,
        }

class Fattura_acquisto(Documento_acquisto):
    data_scadenza = models.DateField('Data di scadenza')
    class Meta:
        verbose_name = 'Fattura di acquisto'
        verbose_name_plural = 'Fatture di acquisto'


class Fattura_acquistoForm(forms.ModelForm):
    #data = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Fattura_acquisto
        widgets = {
            'data_emissione': SuitDateWidget,
            'data_scadenza': SuitDateWidget,
        }