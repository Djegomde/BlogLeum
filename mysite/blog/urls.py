from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.post_list, name='post_list',),
    path('', views.author_list, name='author_list'),
]
