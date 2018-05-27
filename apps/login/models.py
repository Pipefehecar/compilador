# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class usuario(models.Model):

	#usuario = models.OneToOneField(User)
	usuario  = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

	# nombres = models.CharField(max_length=50)
	# apellidos = models.CharField(max_length=50)
	# email = models.EmailField()
	edad = models.IntegerField()
	pais = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	lenguaje = models.CharField(max_length=50)


	# def __str__(self):
	# 	return '{} {}'.format(self.ciudad, self.pais)

	def __unicode__(self):
		return self.usuario.username