from django.shortcuts import render

# Create your views here.
# tworzymy funkcję która bierze żądanie i zwraca wartość z funkcji render
# render złoży nasz template blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})