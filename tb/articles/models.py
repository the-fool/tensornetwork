from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Article(models.Model):
    title = models.TextField()
    summary = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    link = models.URLField()
    vote_count = models.IntegerField(default=0)
    publication_date = models.DateField(auto_now_add=True, editable=False)


class Vote(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
