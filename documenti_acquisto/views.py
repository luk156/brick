# Create your views here.

from documenti_acquisto.models import *
from django.core import urlresolvers
from django.shortcuts import redirect
import datetime as dt

def converti(request, ddt_id):
	ddt = Documento_trasporto.objects.get(id = ddt_id)
	ddt.convertito=True
	ddt.save()
	f=Fattura_acquisto()
	f.fornitore=ddt.fornitore
	f.data_scadenza = dt.datetime.today()
	f.data_emissione = dt.datetime.today()
	f.save()
	for b in ddt.documento_bene.all():
		b.pk=None
		b.documento=f
		b.save()
	return redirect(urlresolvers.reverse('admin:documenti_acquisto_fattura_acquisto_change', args=(f.id,)))
