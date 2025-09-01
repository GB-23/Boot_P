from django.contrib import admin
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.password_reset_by_question, name='password_reset'),
    path('', views.home, name='home'), 
]