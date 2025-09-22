from django.contrib import admin
from .models import Pessoa, Endereco

admin.site.register(Pessoa)
admin.site.register(Endereco)