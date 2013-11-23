# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django import forms
from suit.widgets import SuitDateWidget
from django.contrib.admin import widgets
from ore.models import Attivita, Cliente

# Create your models here.

class Preventivo(models.Model):
    cliente = models.ForeignKey(Cliente)
    data = models.DateField('Data')
    attivita = models.ManyToManyField(Attivita, through='preventivo_attivita')
    def __unicode__(self):
        return u'%s-%s' % (self.cliente, self.data)
    class Meta:
        verbose_name = "Preventivo"
        verbose_name_plural = "Preventivi"
    def totale(self):
        t=0
        for a in self.attivita.objects.all():
            t += a.importo_totale()
        return t
    class Meta:
        verbose_name = "Preventivo"
        verbose_name_plural = "Preventivi"

class preventivo_attivita(models.Model):
    preventivo = models.ForeignKey(Preventivo)
    attivita = models.ForeignKey(Attivita)
    importo_unitario = models.DecimalField('Importo unitario', max_digits=5, decimal_places=2)
    def importo_totale(self):
        return round(self.quantita()*self.importo_unitario,2)
    class Meta:
        verbose_name = "Attività preventivata"
        verbose_name_plural = "Attività preventivate"

class dimensione(models.Model):
    UNITA_MISURA = (
        ('ml.', 'Metri Lineari'),
        ('mq.', 'Metri Quadri'),
        ('mc.', 'Metri Cubi'),
        ('A corpo', 'A corpo'),
        ('Kg.','Kilogrammi'),
        ('Ton.','Tonnelate'),
        )
    preventivo_attivita = models.ForeignKey(preventivo_attivita, related_name='preventivo_attivita_dimensione')
    numero = models.IntegerField('Numero')
    lunghezza = models.DecimalField('Lunghezza', max_digits=5, decimal_places=2, null=True, blank=True,)
    larghezza = models.DecimalField('Larghezza', max_digits=5, decimal_places=2, null=True, blank=True,)
    altezza_peso = models.DecimalField('Altezza/Peso', max_digits=5, decimal_places=2, null=True, blank=True,)
    unita = models.CharField('Unità', choices=UNITA_MISURA, max_length=10, default=1)
    def quantita(self):
        if not self.lunghezza:
            self.lunghezza=1
        if not self.larghezza:
            self.larghezza=1
        if not self.altezza_peso:
            self.altezza_peso=1
        return round(self.numero*self.lunghezza*self.larghezza*self.altezza_peso,2)
    class Meta:
        verbose_name = "Dimensione"
        verbose_name_plural = "Dimensioni"