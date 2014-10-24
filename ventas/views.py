from django.shortcuts import render
from .forms import VentaForm

def venta(request):
	return render(request, "ventas/venta.html")