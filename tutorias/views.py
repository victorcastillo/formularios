# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProcesoAdministrativoForm
import mandrill
from django.template.loader import render_to_string
from django.conf import settings


def enviar_email(html, from_email, subject, to):
	info = {}
	info["html"] = html
	info["from_email"] = from_email
	info["subject"] = subject
	info["to"] = to
	enviar = mandrill.Mandrill(settings.API_KEY_MANDRILL).messages.send(message=info)
	if enviar[0]['status'] == 'sent' or enviar[0]['status'] == 'queued':
		return True
	return False

def proceso_administrativo(request):
	formulario = ProcesoAdministrativoForm()
	if request.method == "POST":
		formulario = ProcesoAdministrativoForm(request.POST)
		if formulario.is_valid():
			usuario = request.user
			matricula = formulario.cleaned_data['matricula']
			nombre_alumno = formulario.cleaned_data['nombre_alumno']
			email_alumno = formulario.cleaned_data['email_alumno']
			proceso = formulario.cleaned_data['proceso']
			from_email = "contacto@utel.edu.mx"
			subject = proceso
			if proceso == "Baja" or proceso == u'Retención':
				to = [{"email": "vcastito@utel.edu.mx", "type":"to", "name": "Ayuda UTEL"}]
			else:
				to = [{"email": "vcastito@utel.edu.mx", "type":"to", "name": "Escolares UTEL"}]
			html = render_to_string('tutorias/proceso.html', locals())
			if enviar_email(html, from_email, subject, to):
				return HttpResponse(u'Petición enviada')
			else:
				return HttpResponse(u'Petición fallida intentelo de nuevo')

	return render(request, 'tutorias/proceso_administrativo.html', locals())

import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def proceso_administrativo_proceso(request):
	proceso = request.GET['proceso'].lower()
	if proceso == "baja":
		html  = "tutorias/baja.html"
	render_ =  render_to_string(html,{})
	return HttpResponse(render_)


def motivo(request):
	motivo = elimina_tildes(request.GET['motivo']).lower().split(' ')[0]
	html = render_to_string('motivos/%s.html' % motivo, {})
	return HttpResponse(html)
