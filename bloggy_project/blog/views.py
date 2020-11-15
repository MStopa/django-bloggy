from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views import generic
from vanilla import ListView, DetailView

import re


class IndexView(generic.ListView):

    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):

        posts = Post.objects.all().order_by('-created_at')
        for post in posts:
            post.url = re.sub(' ', '_', post.title)
        return posts


class PostDetailView(DetailView):

    def get(self, request, *args, **kwargs):

        post = get_object_or_404(Post, title=kwargs['url'].replace('_', ' '))
        post.views += 1
        post.save()
        return render(request,
                     'blog/post.html',
                     {'single_post': post})
