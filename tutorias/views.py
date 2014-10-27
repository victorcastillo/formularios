# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
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
	import collections
	if request.method == "POST":
		variables =  dict(request.POST.copy())
		del variables['csrfmiddlewaretoken']
		para_tabla = {}
		for variable,valor in variables.iteritems():
			valor = ", ".join(valor)
			para_tabla[variable] = variable.replace('_',' ').capitalize() +' : ' + valor
		content_table = ''
		para_tabla = collections.OrderedDict(sorted(para_tabla.items()))
		for c,v in para_tabla.iteritems():
			content_table += '<tr><td> %s </td></tr>' % v
		
		tabla = '<table border="1">%s</table>' % content_table
		
		from_email = "contacto@utel.edu.mx"
		subject = para_tabla['proceso']
		proceso = variables['proceso']
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
	proceso = elimina_tildes(request.GET['proceso']).lower().split(' ')[0]
	html  = "tutorias/%s.html" % proceso
	render_ =  render_to_string(html,{})
	return HttpResponse(render_)


def motivo(request):
	motivo = elimina_tildes(request.GET['motivo']).lower().split(' ')[0]
	html = render_to_string('motivos/%s.html' % motivo, {})
	return HttpResponse(html)

def servicio(request):
	servicio = elimina_tildes(request.GET['servicio']).lower().split(' ')[0]
	html =  render_to_string('servicios/%s.html' % servicio, {})
	return HttpResponse(html)