from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, user_logged_in
from django.shortcuts import render
from django import forms
from home.models import CustomUser
from postagem.models import Postagem
from home.forms import CustomUserCreationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email','role']


def home(request):
    # Busca as últimas 4 postagens publicadas e as exibe na página inicial
    ultimas_postagens = Postagem.objects.order_by('id')[:4]
    if request.user.is_authenticated:
        role = request.user.role
    else:
        role = None
    return render(request, 'home.html', {'user':request.user, 'ultimas_postagens':ultimas_postagens, 'role':role})

def register_view(request):
    # Lida com a lógica de registro de novos usuários
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password') or form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    # Trata a lógica de login do usuário
    if request.method == 'POST':
        form = LoginView.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    return render(request, 'login.html', {'form':LoginView.form_class})

def profile_view(request):
    # Renderiza a página de perfil do usuário autenticado
    posts_usuario = Postagem.objects.filter(autor=request.user)
    return render(request, 'profile.html', {'user':request.user, 'postagem':Postagem.objects.all(),'post_usuario':posts_usuario})

def logout_view(request):
    # Lida com a lógica de logout
    logout(request)
    return render(request, 'home.html')
