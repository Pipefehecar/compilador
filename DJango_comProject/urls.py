"""DJango_comProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.auth.views import login

from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
admin.autodiscover()

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

     #PYTHON SOCIAL AUTH
    #url(r'',include('social.apps.django_app.urls', namespace= 'social'  )),

    #django_social    
    url(r'^account/',include('social_django.urls', namespace= 'social'  )),    
    url(r'^account/',include('django.contrib.auth.urls', namespace= 'auth')),    


    url(r'^usuario/',include('apps.login.urls', namespace='usuario')),

    #login
    url(r'^login', login, {'template_name':'login/index.html'}, name='login'),
    #logout
    url(r'^logout', logout, {'template_name':'login/index.html'}, name='logout'),

    #reestablecimiento de contrasenia
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html','email_template_name':'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done', password_reset_done, {'template_name':'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name':'registration/password_reset_confirm.html'},name ='password_reset_confirm'),
    url(r'^reset/done$', password_reset_complete,{'template_name':'registration/password_reset_complete.html'},name ='password_reset_complete'),
]
