from django.db.migrations import serializer
from django.shortcuts import render, redirect
from postagem.forms import PostagemForm
from postagem.models import Postagem
from rest_framework.views import APIView
from rest_framework.response import Response

from postagem.serializers import PostagemSerializer


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

def edit_post(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES, instance=postagem)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = PostagemForm(instance=postagem)

    return render(request,'edit.html', {'form':form})

class PostagemAPIView(APIView):
    def get(self,request):
        postagem = Postagem.objects.all()
        serializer = PostagemSerializer(postagem, many=True)
        return Response(serializer.data)