from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django import forms
from suit.widgets import SuitDateWidget
from django.contrib.admin import widgets

class Cliente(models.Model):
	nome = models.TextField('Nome', max_length=30)
	cognome = models.TextField('Cognome', max_length=, null=True, blank=True)
	mail = models.EmailField('E-Mail', null=True, blank=True)
	telefono = models.IntegerField('Telefono principale', null=True, blank=True)
	indirizzo = models.TextField('Indirizzo', max_length=100, null=True, blank=True)
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.cognome)
	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clienti"

class Cantiere(models.Model):
	descrizione = models.TextField('Descrizione', max_length=100)
	indirizzo = models.TextField('Indirizzo', max_length=100, null=True, blank=True)
	cliente = models.ForeignKey(Cliente, related_name='cliente_cantiere')
	def __unicode__(self):
		return u'%s' % (self.descrizione)
	class Meta:
		verbose_name = "Cantiere"
		verbose_name_plural = "Cantieri"

class Dipendente(models.Model):
	nome = models.TextField('Nome', max_length=30)
	cognome = models.TextField('Cognome', max_length=30)
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.cognome)
	class Meta:
		verbose_name = "Dipendente"
		verbose_name_plural = "Dipendenti"

class Categoria_mansione(MPTTModel):
	nome = models.TextField('Nome', max_length=30)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
	def __unicode__(self):
		return u'%s' % (self.nome)
	class Meta:
		verbose_name = "Categoria della mansioni"
		verbose_name_plural = "Categorie delle mansioni"
	class MPTTMeta:
		order_insertion_by = ['nome']



class Mansione(models.Model):
	nome = models.TextField('Nome', max_length=30)
	categoria = models.ForeignKey(Categoria_mansione, related_name='categoria_mansione' )
	def __unicode__(self):
		return u'%s ( %s )' % (self.nome, self.categoria)
	class Meta:
		verbose_name = "Mansione"
		verbose_name_plural = "Mansioni"

class Scheda_lavoro(models.Model):
	dipendente = models.ForeignKey(Dipendente, related_name='dipendente_scheda')
	cantiere = models.ForeignKey(Cantiere, related_name='cantiere_scheda')
	ore = models.IntegerField('Ore Lavorative')
	mansione = models.ForeignKey(Mansione, related_name='mansione_scheda')
	ext_preventivo = models.BooleanField('Fuori preventivo', default=False)
	data = models.DateField()
	def __unicode__(self):
		return u'%s (%s) - %s' % (self.id, self.dipendente, self.data)
	class Meta:
		verbose_name = "Scheda lavoro"
		verbose_name_plural = "Schede lavoro"

class Scheda_lavoroForm(forms.ModelForm):
	#data = forms.DateField(widget=widgets.AdminDateWidget)
	class Meta:
		model = Scheda_lavoro
		widgets = {
			#'data': SuitDateWidget,
		}
