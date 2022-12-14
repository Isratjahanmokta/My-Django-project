from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.models import User
from App_login.models import Follow
from App_post.models import Post, Like
# Create your views here.

@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    print(liked_post_list)
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains = search)
    return render(request, 'App_post/home.html', context = {'title':'Home', 'search':search, 'result':result, 'posts': posts, 'liked_post_list': liked_post_list})

@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user=user)
    if not already_liked:
        liked_post = Like(post=post, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(post=post, user = user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))