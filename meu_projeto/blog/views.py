from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Pessoa, Endereco
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder

def login_check(request):
    if not request.user.is_authenticated:
        return redirect('login')  


@login_required  
def lista_endereco(request):
    pessoas = Pessoa.objects.select_related('usuario').prefetch_related('enderecos').all()
    
    pessoas_data = []
    for pessoa in pessoas:
        enderecos_data = []
        for end in pessoa.enderecos.all():
            enderecos_data.append({
                'id': end.id,
                'rua': end.rua,
                'numero': end.numero,
                'bairro': end.bairro,
                'cidade': end.cidade,
                'estado': end.estado,
                'cep': end.cep,
            })
        pessoas_data.append({
            'id': pessoa.id,
            'nome': pessoa.nome,
            'usuario': pessoa.usuario.username,
            'enderecos': enderecos_data,
        })
    
    context = {
        'pessoas_json': json.dumps(pessoas_data, cls=DjangoJSONEncoder)
    }
    return render(request, 'index.html', context)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
          
            login(request, user)
            return redirect('home') 
        else:
           
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, "logout.html")  # Or wherever you want to redirect after logout


def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')


def alterar_senha(request):
    return render(request, 'alterar_senha.html')


def cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
            return render(request, 'cadastrar.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está em uso.')
            return render(request, 'cadastrar.html')

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('login') 

    return render(request, 'cadastrar.html')


@login_required
def perfil(request):
    return render(request, 'perfil.html')


@login_required
def home(request):
    return render(request, 'home.html')


def erro_404(request, exception):
    return render(request, '404.html', status=404)


def erro_403(request, exception):
    return render(request, '403.html', status=403)


def erro_500(request):
    return render(request, '500.html', status=500)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    
    pessoas_data = []
    for p in pessoas:
        pessoas_data.append({
            'id': p.id,
            'nome': p.nome,
            'cpf': p.cpf,
            'email': p.email,
            'telefone': p.telefone,
        })
    
    context = {
        'pessoas_json': json.dumps(pessoas_data, cls=DjangoJSONEncoder)
    }
    return render(request, 'lista_pessoas.html', context)
