from django.shortcuts import render, get_object_or_404 # przy braku posta o danym id zwraca błąd 404
from django.utils import timezone
from .models import Post # Importujemy nasz model Post

# Tworzymy funkcję która bierze żądanie i zwraca wartość z funkcji render
# render złoży nasz template blog/post_list.html
def post_list(request):
    # Tworzymy zmienną 'posts' dla naszego QuerySetu i ustawiamy filtrowanie wg daty publikacji postu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts}) # Przekazujemy dane do naszego szablonu 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
