from django.urls import path
from .views import PostagemAPIView

urlpatterns = [
    path('postagens/', PostagemAPIView.as_view()),
]