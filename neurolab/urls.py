from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('investigaciones', views.investigaciones, name='investigaciones'),
    path('accounts/login/', LoginView.as_view(template_name='paginas/iniciarSesion.html'), name='iniciarSesion'),
    path('logout', logout_then_login, name='logout'),
    path('contactenos', login_required(views.contactenos), name='contactenos'),

    path('familiaCuidador', views.familiaCuidador, name='familiaCuidador'),
    path('pam', views.pam, name='pam'),
    path('personalAcreditado', views.personalAcreditado, name='personalAcreditado'),

    path('capacitacionCuidados', views.capacitacionCuidados, name='capacitacionCuidados'),
    path('edm', views.edm, name='edm'),
    path('enc', views.enc, name='enc'),
    path('isa', views.isa, name='isa'),
    path('reporteClinico', views.reporteClinico, name='reporteClinico'),

    path('prueba1', views.prueba1, name='prueba1'),
    path('registroPaciente', login_required(views.registroPaciente), name='registroPaciente'),

    path('bienvenido', views.bienvenido, name='bienvenido'),
]