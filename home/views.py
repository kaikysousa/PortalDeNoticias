from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
import logging
from home.forms import CustomUserCreationForm
from django.shortcuts import render
from django import forms

from home.models import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email','is_reader','is_journalist']
def home(request):
    # Renderiza a página inicial
    return render(request, 'home.html')
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash a senha
            user.save()  # Salva o usuário no banco de dados
            forms.clean()
            login(
                request, user
            )
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info("Função login sendo chamada")