from django import forms

from models import usuario

from django.contrib.auth.models  import User
from django.contrib.auth.forms  import UserCreationForm 

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'first_name',
				'last_name',
				'username',
				'email',
				'password'
			]
		labels= {
				'first_name':'Nombre de usuario',
				'last_name':'Nombre',
				'username':'Apellidos',
				'email':'E-mail',
				'password': 'Clave',
			}



			# -*- encoding:utf-8 -*-


class UsuarioForm(forms.ModelForm):

	class Meta:
		model = usuario
		fields = [
			'edad',
			'ciudad',
			'pais',
			'lenguaje',
			'usuario',
		]
		labels = {
			'edad': 'Edad',
			'ciudad': 'Ciudad de origen',
			'pais': 'Pais de origen',
			'lenguaje': 'Lenguaje de preferencia',
			'usuario' : 'Id usuario',
		}
