# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Article


def index(request):
    latest_articles = Article.objects.order_by('-publication_date')[:5]
    context = {'articles': latest_articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})
