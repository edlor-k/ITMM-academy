from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        'title': 'Главная страница',
        'articles': articles,
        }
    return render(request, 'main/home.html', context)