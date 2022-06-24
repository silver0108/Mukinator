from django.contrib.auth import authenticate, login, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm, UserUpdateForm
from community.models import Post
from django.core.paginator import Paginator


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required
def update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'common/mypage.html', {'form': form})
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'common/user_update.html', {'form': form})


def mypage(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'common/mypage.html', context)


def mypost(request, pk):
    post_list = Post.objects.order_by('-create_date')
    sort = request.GET.get('sort', '')
    page = request.GET.get('page', 1)
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    context = {'user': user, 'post_list': page_obj, 'page': page, 'sort': sort}
    return render(request, 'common/mypost.html', context)

