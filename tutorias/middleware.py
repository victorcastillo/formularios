from .models import UserUrl, Url
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


class UrlMiddleware(object):

	def process_request(self,request):
		if not request.user.is_authenticated():
			raise Http404
		if (not request.path.startswith("/admin")) and (not request.is_ajax()):
			usuario = request.user
			url = get_object_or_404(Url, url=request.path, habilitada=True)
			url_usuario = UserUrl.objects.filter(url=url, user=usuario)
			if not url_usuario:
				return HttpResponse(content="No puedes ver esta URL", status=403)