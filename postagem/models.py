from django.db import models

class Postagem(models.Model):
    tags = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d', null=True, blank=True )
    autor = models.ForeignKey('home.CustomUser', on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo
