from django.urls import path 
from . import views # importujemy wyświetlenia z bloga

# dodajemy nasz pierwszy wzór url
urlpatterns = [
    path('', views.post_list, name='post_list')
]