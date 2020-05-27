from django.conf import settings
from django.db import models
from django.utils import timezone

# Tworzymy model 'Post' dla naszych postów na blogu 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # Definiujemy ilość znaków w tytule 
    text = models.TextField() # Tu będzie nasz wpis na bloga
    created_date = models.DateTimeField(default=timezone.now) # Data stworzenia posta
    published_date = models.DateTimeField(blank=True, null=True) # Data opublikowania posta
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # metoda zwraca sama siebie, czyli wywołując __string__() otrzymamy tytuł
    def __str__(self):
        return self.title
