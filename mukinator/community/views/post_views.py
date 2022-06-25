from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import PostForm
from ..models import Post, Photo


@login_required(login_url='common:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.post = post
                photo.image = img
                photo.save()
            return redirect('community:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'community/post_form.html', context)


@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('community:detail', post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()
            post.save()
            return redirect('community:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'check': True}
    return render(request, 'community/post_form.html', context)


@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('community:detail', post_id=post.id)
    post.delete()
    return redirect('community:index')
