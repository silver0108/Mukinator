from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import CommentForm
from ..models import Post, Comment


@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('community:detail', post_id=post.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'post': post, 'form':form}
    return render(request, 'community/post_detail.html', context)


@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, pk=comment.post.id)
    check = False
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('community:detail', comment_id=comment.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('community:detail', post_id=comment.post.id)
    else:
        check = True
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form, 'check': check, 'post': post, 'comment_id': comment_id}
    return render(request, 'community/post_detail.html', context)


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('community:detail', post_id=comment.post.id)