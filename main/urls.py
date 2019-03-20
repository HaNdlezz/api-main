"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import core.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name="index"),
    url(r'^$', views.login_user, name="login"),
	url(r'^upload/$', views.upload, name="upload"),
    url(r'^API_GENERAL/$', views.API_GENERAL, name="API_GENERAL"),
    url(r'^API_ANUAL/$', views.API_ANUAL, name="API_ANUAL"),
	url(r'^API_POST/$', views.API_POST, name="API_POST"),
    url(r'^upload_docente/$', views.upload_docente, name="upload_docente"),
    url(r'^search/$', views.search, name="search"),
    url(r'^carga_evaluacion_docente/$', views.carga_evaluacion_docente, name="carga_evaluacion_docente"),
    url(r'^details_evaluacion_docente/$', views.details_evaluacion_docente, name="details_evaluacion_docente"),

]
