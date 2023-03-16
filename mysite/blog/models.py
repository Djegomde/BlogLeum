from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    photo_profil = models.ImageField(upload_to='static/images', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo_post = models.ImageField(upload_to='static/images', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
