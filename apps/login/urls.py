# from django.conf.urls import url, include
# # from views import index, registrarse, home
# from views import registrarse, home
 
# urlpatterns = [
#     # url(r'^$', 'apps.login.views.index'),
#     # url(r'^$', views.index, name='index'),
#     # url(r'^$', index.as_view(), name='login'),
#     url(r'^registrarse/$', registrarse.as_view(), name='registrarse'),
#     url(r'^home/$', home.as_view(), name='home'),

#     # url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login/index.html'}, name='login'),

#     # url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
# ]


#########################################
# RegistroUsuario = registrarse
# HomeUsuario = home


from django.conf.urls import url
from views import registrarse, home
#from apps.usuario.views import RegistroUsuario, HomeUsuario
from django.contrib.auth.views import login_required

urlpatterns = [
	# url(r'^registrarse/$', registrarse.as_view(), name='registrarse'),
 #    url(r'^home/$', home.as_view(), name='home'),

	url(r'^registrarse/$', registrarse, name='registrarse'),
    url(r'^home/$', home, name='home'),


]