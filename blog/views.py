from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone  
from .models import Post
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            created_at=timezone.now(),
        )

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                "type": "send_new_post",
                "post": {
                    "title": post.title,
                    "content": post.content,
                    "author": post.author.username,
                    "created_at": post.created_at.strftime("%Y-%m-%d %H:%M"),
                    "action": "created",
                }
            }
        )
        return redirect('post_list')
    return render(request, 'blog/create_post.html')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You cannot edit this post.")

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden('You cannot delete this post.')

    if request.method == 'POST':
        deleted_post_id = post.id
        post_title = post.title
        post.delete()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                "type": "send_new_post",
                "post": {
                    "id": deleted_post_id,
                    "title": post_title,
                    "action": "deleted",
                }
            }
        )
        return redirect('post_list')
    return HttpResponseForbidden('Invalid request')
