from django.contrib import admin
from django.contrib.auth.models import User

from .models import Url, UserUrl

class UrlUserAdmin(admin.ModelAdmin):
	model = UserUrl

class UrlAdmin(admin.ModelAdmin):
	model = Url


  

admin.site.register(Url,UrlAdmin)
admin.site.register(UserUrl,UrlUserAdmin)
