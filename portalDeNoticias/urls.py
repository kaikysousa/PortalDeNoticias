from django.contrib import admin
from django.urls import path
from home import views  # Importando as views do seu app "home"
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from home.views import register_view, logout_view, login_view

urlpatterns = [
    # URL para o admin
    path('admin/', admin.site.urls),

    # URL para a homepage
    path('', views.home, name='home'),

    # URL para o registro de um novo usuário
    path('register/', register_view, name='register'),

    # URL para o login
    path('login/', login_view, name='user_login'),

    # URL para o logout (usando o logout padrão do Django)
    path('logout/', views.logout_view, name='user_logout'),

    path('profile/', views.profile_view, name='user_profile')
]

# Adicionando os arquivos estáticos e de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
