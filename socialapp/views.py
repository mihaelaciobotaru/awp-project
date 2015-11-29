from django.shortcuts import render, redirect

from socialapp.models import UserPost, UserPostComment
from socialapp.forms import UserPostForm, UserPostCommentForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.order_by('-date_added')
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text)
            user_post.save()
        return redirect('index')


def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        comments = UserPostComment.objects.filter(post_id=post).order_by('-date_added')
        form = UserPostCommentForm()
        context = {'post': post,
                   'form': form,
                   'comments': comments,
                   }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post_comment = UserPostComment(text=text, post=post)
            user_post_comment.save()
        return redirect('post_details', pk=pk)


