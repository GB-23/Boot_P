from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, PasswordResetByQuestionForm
from .models import CustomUser, Profile 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def password_reset_by_question(request):
    if request.method == 'POST':
        form = PasswordResetByQuestionForm(request.POST)
        if form.is_valid():
            try:
                user = CustomUser.objects.get(username=form.cleaned_data['username'])
                profile = Profile.objects.get(user=user)
                if profile.check_answer(form.cleaned_data['answer']):
                    user.set_password(form.cleaned_data['new_password1'])
                    user.save()
                    messages.success(request, 'Senha resetada com sucesso!')
                    return redirect('login')
                else:
                    messages.error(request, 'Resposta incorreta')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Usuário não encontrado')
    else:
        form = PasswordResetByQuestionForm()

        # Se GET com username, mostra a pergunta
        username = request.GET.get('username')
        question = None
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                profile = Profile.objects.get(user=user)
                question = profile.security_question
            except CustomUser.DoesNotExist:
                messages.error(request, 'Usuário não encontrado')

    return render(request, 'accounts/password_reset.html', {'form': form, 'question': question})

@login_required
def home(request):
    return render(request, 'home.html')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')