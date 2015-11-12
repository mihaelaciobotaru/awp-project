from django.shortcuts import render

from socialapp.models import UserPost


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'index.html', context)
