from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
import logging
from home.forms import CustomUserCreationForm
from django.shortcuts import render

def home(request):
    # Renderiza a página inicial
    return render(request, 'home.html')
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_reader = form.cleaned_data['is_reader']
            user.is_journalist = form.cleaned_data['is_journalist']
            user.save()
            login(request, user)  # Autentica o usuário
            return redirect('home')  # Redireciona para a homepage
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info("Função login sendo chamada")