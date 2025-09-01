from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('recuperar-senha/', views.recuperar_senha, name='recuperar_senha'),
]
