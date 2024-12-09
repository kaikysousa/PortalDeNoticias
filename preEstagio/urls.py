from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
from home.views import register_view, logout_view, login_view, profile_view
from postagem import views as views_postagem

urlpatterns = [
    # URL para o admin
    path('admin/', admin.site.urls),

    # URL para a homepage
    path('', views.home, name='home'),

    # URLs de autenticação
    path('register/', register_view, name='register'),
    path('login/', login_view, name='user_login'),
    path('logout/', logout_view, name='user_logout'),

    # URL para o perfil do usuário
    path('profile/', profile_view, name='user_profile'),

    # URLs relacionadas a postagens
    path('post/', views_postagem.post_view, name='post_view'),
    path('post_detail/<int:pk>/', views_postagem.post_detail, name='post_detail'),
]

# Serve arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)