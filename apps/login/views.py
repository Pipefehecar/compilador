# # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
# # from django.shortcuts import render_to_response
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models  import User
from django.contrib.auth.forms  import UserCreationForm 
from forms import RegistroForm
# # Create your views here.
# # def index(request):
# # 	return render_to_response('login/index.html')
# # class index(TemplateView):
# # 	template_name = 'login/index.html'

# class home(TemplateView):
#  	template_name = 'login/compilador.html'

# class registrarse(CreateView):
#  	model = User
#  	template_name = 'login/registrarUsuario.html'
#  	form_class = RegistroForm 
#  	success_url = reverse_lazy('')
#  	#fields = '__all__'
from django.template import RequestContext

from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User #Usuario Django por defecto
from django.contrib.auth.forms import UserCreationForm

from models import usuario #Usuario (comunidad)
from forms import UsuarioForm, RegistroForm

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages
import json
#RegistroUsuario = registrarse
#HomeUsuario = home
def registrarse(request):

	answer = 0
	  

	 #1 = duplicado
	 #2 = registrado 

	if request.method == 'POST':
		print("Se realizo una peticion: POST\n")

		print("Obteniendo los request para [ User ]")
		username   = request.POST['username']
		first_name = request.POST['first_name']
		last_name  = request.POST['last_name']
		email  = request.POST['email']
		password1  = request.POST.get('password1')
		password2 = request.POST.get('password2')

		print("Obteniendo los request para [ Ususuario ]")
		edad	 = request.POST['edad']
		ciudad    = request.POST['ciudad']
		pais     = request.POST['pais']
		lenguaje = request.POST['lenguaje']

		lista = User.objects.filter(username = username, email = email)

		if lista : #Si (list_message != Vacia): return (False), No es vacia (True)
			print(" !!! objeto duplicado")
			answer = 1

		else:
			answer = 2			
			user = User.objects.create_user(username, email, password1)
			user.last_name = last_name.title()
			user.first_name = first_name.title()
			user.save()

			# us = usuario(edad = edad, ciudad = ciudad.title(), pais = pais.title(), 
			# lenguaje = lenguaje.title(), usuario_id = user.id)
			# us.save()

	return render(request,'login/registrarUsuario.html',{"respuesta":answer}) 
	# return render_to_response("login/registrarUsuario.html",RequestContext(request,{"respuesta":answer})) 

def home(request):
	return render(request,'login/compilador.html')


	