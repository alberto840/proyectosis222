from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('investigaciones', views.investigaciones, name='investigaciones'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
    path('contactenos', views.contactenos, name='contactenos'),

    path('familiaCuidador', views.familiaCuidador, name='familiaCuidador'),
    path('pam', views.pam, name='pam'),
    path('personalAcreditado', views.personalAcreditado, name='personalAcreditado'),

    path('capacitacionCuidados', views.capacitacionCuidados, name='capacitacionCuidados'),
    path('edm', views.edm, name='edm'),
    path('enc', views.enc, name='enc'),
    path('isa', views.isa, name='isa'),
    path('reporteClinico', views.reporteClinico, name='reporteClinico'),

    path('prueba1', views.prueba1, name='prueba1'),
    path('registroPaciente', views.registroPaciente, name='registroPaciente'),
]