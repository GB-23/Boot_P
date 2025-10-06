from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('lista-pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('index/', views.lista_endereco, name='index'),
    path('homeadmin/', views.homeadmin, name='homeadmin'),
    path('homemanager/', views.homemanager, name='homemanager'),
]
