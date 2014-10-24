# -*- coding: utf-8 -*-
from django import forms

class VentaForm(forms.Form):
	SUPERVISORES = (
		(u'Heras Serrano José Antonio', u'Heras Serrano José Antonio'),
		(u'Hernández López María de Jesús', u'Hernández López María de Jesús'),
		(u'Mondragón Fragoso Luis Xavier', u'Mondragón Fragoso Luis Xavier'),
		(u'Olivares Barragán Francisco Javier', u'Olivares Barragán Francisco Javier'),
		(u'Otero Martín del Campo Rocío', u'Otero Martín del Campo Rocío'),
		(u'Ruiz Herrera Marlen', u'Ruiz Herrera Marlen'),
		(u'Sierra Juárez Dulce Damaris', u'Sierra Juárez Dulce Damaris'),
	)

	LICENCIATURAS = (
		(u'Administración',u'Administración'),
		(u'Administración de negocios',u'Administración de negocios'),
		(u'Administración de recursos humanos',u'Administración de recursos humanos'),
		(u'Administración y finanzas',u'Administración y finanzas'),
		(u'Administración de tecnologías de información',u'Administración de tecnologías de información'),
		(u'Contaduría pública',u'Contaduría pública'),
		(u'Contaduría y finanzas',u'Contaduría y finanzas'),
		(u'Ingeniería en sistemas computacionales',u'Ingeniería en sistemas computacionales'),
		(u'Ingeniería industrial',u'Ingeniería industrial'),
		(u'Ingeniería industrial y administración',u'Ingeniería industrial y administración'),
		(u'Mercadotecnia',u'Mercadotecnia'),
		(u'Negocios internacionales',u'Negocios internacionales'),
		(u'Pedagogía',u'Pedagogía'),
		(u'Psicología organizacional',u'Psicología organizacional'),
		(u'Comunicación',u'Comunicación'),
		(u'Comunicación Digital',u'Comunicación Digital'),
		(u'Comunicación Organizacional',u'Comunicación Organizacional'),
		(u'Derecho',u'Derecho'),
	)
	
	JORNADAS = (
		(u'Reducidas','r'),

	)

	nombre_alumno = forms.CharField(max_length=100, required=True)
	correo_alumno = forms.CharField(max_length=100, required=True)
	supervisor = forms.ChoiceField(required=True, choices=SUPERVISORES)
	deposito = forms.DecimalField(required=True)
	fecha_pago = forms.DateField(required=True)
	licenciatura = forms.ChoiceField(required=True, choices=LICENCIATURAS)
	jornada = forms.ChoiceField(required=True, choices=JORNADAS)
	ciclo_inicio = forms.DateField(required=True)
	tipo_ingreso = forms.ChoiceField(required=True)
	estatus = forms.ChoiceField(required=True)
	mes_venta = forms.ChoiceField(required=True)
	id_admisiones = forms.IntergerField(required=True)
	id_sugar = forms.IntergerField(required=True)
	observaciones = forms.TextField()
