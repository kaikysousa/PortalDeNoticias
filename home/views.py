from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, user_logged_in
from django.shortcuts import render
from django import forms

from home.models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email','role']
def home(request):
    role = request.user.role
    return render(request, 'home.html', {'user':request.user})
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash a senha
            user.save()  # Salva o usuário no banco de dados
            login(
                request, user
            )
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginView.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    return render(request, 'login.html', {'form':LoginView.form_class})
def profile_view(request):
    return render(request, 'profile.html', {'user':request.user})

def logout_view(request):
    logout(request)
    return render(request, 'home.html')
