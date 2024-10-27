from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

@login_required
def home(request):
    articles = Article.objects.all()
    context = {
        'title': 'Главная страница',
        'articles': articles,
        }
    return render(request, 'main/home.html', context)

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = ArticleForm()
    return render(request, 'main/add_article.html', {'form': form}) 