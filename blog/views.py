from django.shortcuts import render, get_object_or_404, redirect # przy braku posta o danym id zwraca błąd 404
from django.utils import timezone
from .models import Post # Importujemy nasz model Post
from .forms import PostForm # Importujemy model PostForm

# Tworzymy funkcję która bierze żądanie i zwraca wartość z funkcji render
# render złoży nasz template blog/post_list.html
def post_list(request):
    # Tworzymy zmienną 'posts' dla naszego QuerySetu i ustawiamy filtrowanie wg daty publikacji postu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) # Przekazujemy dane do naszego szablonu 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # po zapisaniu przekierowuje nas na nowo utworzony wpis(widok post_detail)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})