from django.contrib import admin
from .models import Pessoa, Endereco

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'tipo', 'email')
    list_filter = ('tipo',)
    search_fields = ('nome', 'usuario__username', 'email')
    fields = ('usuario', 'nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'rg', 'endereco', 'bairro', 'tipo')

    
admin.site.register(Endereco)