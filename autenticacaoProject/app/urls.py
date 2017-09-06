from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [

    url(r'^registrar_usuario/$', registrar_usuario, name='registrar_usuario'),
    url(r'^listar_usuario/$',listar_usuario, name='listar_usuario'),

]
