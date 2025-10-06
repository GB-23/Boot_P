from django.urls import path
from . import views

urlpatterns = [
    # ...existing code...
    path('erro_403/', views.erro_403, name='erro_403'),
]