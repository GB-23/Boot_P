from django.shortcuts import render
from .models import Pessoa, Endereco
from django.views.decorators.csrf import csrf_exempt

#teste
def lista_endereco(request):
    pessoas = Pessoa.objects.select_related('usuario').prefetch_related('enderecos')
    return render(request, 'index.html', {'pessoas': pessoas})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        print(f"Usuário: {usuario} | Senha: {senha}", flush=True) #teste pra visualizar
    return render(request, 'login.html')


def logout_view(request):
    return render(request, 'logout.html')

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')

def alterar_senha(request):
    return render(request, 'alterar_senha.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def perfil(request):
    return render(request, 'perfil.html')

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
    return render(request, 'lista_pessoas.html', {'pessoas': pessoas})