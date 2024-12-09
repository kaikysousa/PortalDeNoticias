from django.shortcuts import render, redirect
from postagem.forms import PostagemForm
from postagem.models import Postagem


def post_view(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            postagem.usuario = request.user
            postagem.save()
            form = PostagemForm()
            return redirect('home')
    else:
        form = PostagemForm()

    return render(request, 'postagem.html', {'form': form})

def post_detail(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    return render(request, 'postDetail.html', {'postagem':postagem})