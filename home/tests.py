from django.test import TestCase
from django.urls import reverse

from home.models import CustomUser
from postagem.models import Postagem


class PublicPagesTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_login_page_renders(self):
        response = self.client.get(reverse("user_login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_post_api_lists_posts(self):
        response = self.client.get("/api/v1/postagens/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


class PostagemModelTests(TestCase):
    def test_str_returns_title(self):
        user = CustomUser.objects.create_user(
            username="kaiky",
            email="kaiky@example.com",
            password="senha-forte-123",
        )
        post = Postagem.objects.create(
            tags="teste",
            titulo="Titulo de teste",
            conteudo="Conteudo",
            autor=user,
        )

        self.assertEqual(str(post), "Titulo de teste")
        self.assertFalse(post.publicada)
