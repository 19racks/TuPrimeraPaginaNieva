from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'blog/inicio.html', {'posts': posts})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()
    return render(request, 'blog/agregar_autor.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'blog/agregar_categoria.html', {'form': form})

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})

def buscar_post(request):
    if request.method == 'POST':
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Post.objects.filter(titulo__icontains=termino)
            return render(request, 'blog/buscar_post.html', {'form': form, 'resultados': resultados})
    else:
        form = BuscarPostForm()
    return render(request, 'blog/buscar_post.html', {'form': form})