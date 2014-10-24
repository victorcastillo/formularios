# -*- coding: utf-8 -*-

from django import forms


class ProcesoAdministrativoForm(forms.Form):
	
	PROCESO_CHOICES = (
        (None, '--------'),
        (u'Baja', u'Baja'),
        (u'Retención', u'Retención'),
        (u'Cambio de ciclo', u'Cambio de ciclo'),
        (u'Baja de materias', u'Baja de materias'),
        (u'Cancelación de venta', u'Cancelación de venta'),
        (u'Actualización de datos en Admisiones y/o materias de Aula virtual', u'Actualización de datos en Admisiones y/o materias de Aula virtual'),
        (u'Reducción o incremento de jornada', u'Reducción o incremento de jornada'),
        (u'Cambio de licenciatura', u'Cambio de licenciatura'),
        (u'Cambio de materias', u'Cambio de materias'),
    )
	matricula = forms.CharField(required=True)
	nombre_alumno = forms.CharField(required=True)
	email_alumno = forms.EmailField(required=True)
	proceso = forms.ChoiceField(required=True, choices=PROCESO_CHOICES)