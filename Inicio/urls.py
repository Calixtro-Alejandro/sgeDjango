from django.urls import path
from . import views

urlpatterns=[
    path('', views.Inicio, name='Inicio'),
    #path('<str:nombre>/', views.Saludo, name='Saludo'),
    path('SGE/', views.SGE, name='SGE'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('Blog/', views.Blog, name='Blog'),
    path('CyberSeguridad/', views.CyberSeguridad, name='CyberSeguridad'),
    path('Usuario/', views.Usuario, name='Usuario'),


]
