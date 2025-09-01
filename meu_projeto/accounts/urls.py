from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('perfil/', views.profile, name='perfil'),
   # path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('password-reset/', views.password_reset_by_question, name='password_reset'),
]
