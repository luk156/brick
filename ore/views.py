from ore.models import *
from django.shortcuts import render_to_response, redirect, render
# Create your views here.
def list_dipendenti(request):
	dipendenti = Dipendente.objects.all()
	return render(request,'dipendenti.html',{'request':request,'dipendenti': dipendenti,})