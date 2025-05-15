from django.shortcuts import render # type: ignore
from django.views import generic
from .models import Post

#  Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "post_list.html"
