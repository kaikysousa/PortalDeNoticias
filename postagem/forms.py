from django import forms
from postagem.models import Postagem


class PostagemForm(forms.ModelForm):

    class Meta:
        model = Postagem
        fields = ['titulo', 'conteudo','imagem','tags']

    def __init__(self, *args, **kwargs):
        super(PostagemForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['conteudo'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagem'].required = False
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].required = False