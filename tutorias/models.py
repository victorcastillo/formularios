from django.db import models

from django.contrib.auth.models import User

class Url(models.Model):
	url = models.CharField(max_length=100)
	users = models.ManyToManyField(User, through='UserUrl')
	habilitada = models.BooleanField(default=True)

	def __unicode__(self):
		return self.url

class UserUrl(models.Model):
	url = models.ForeignKey(Url)
	user = models.ForeignKey(User)

