from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upload_docente/$', views.upload_docente, name="upload_docente"),
    url(r'^search/$', views.search, name="search"),
    url(r'^details_evaluacion_docente/$', views.details_evaluacion_docente, name="details_evaluacion_docente"),
    url(r'^carga_evaluacion_docente/$', views.carga_evaluacion_docente, name="carga_evaluacion_docente"),
#    url(r'^bitacora/(?P<pk>\d+)$',views.bitacora, name="bitacora"),


]