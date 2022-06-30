from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy
from common.forms import UserForm, UserUpdateForm
from community.models import Post
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from common.models import User
from django.core.mail import EmailMessage
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.translation import gettext_lazy as _




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


def forget_id(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                template = render_to_string('common/id_email_template.html', {'nickname': user.nickname, 'id': user.username})
                method_email = EmailMessage(
                    '[먹키네이터] 회원님의 아이디를 알려드립니다.',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                method_email.send(fail_silently=False)
                return render(request, 'common/id_sent.html', context)
        except:
            messages.info(request, "There is no username along with the email!")
    return render(request, 'common/forget_id.html', context)


class UserPasswordResetView(PasswordResetView):
    template_name = 'common/password_reset_form.html'
    success_url = reverse_lazy('common:password_reset_done')
    form_class = PasswordResetForm
    email_template_name = "common/password_reset_email.html"

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'common/password_reset_done_fail.html')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'common/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('common:password_reset_complete')
    template_name = 'common/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'common/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context
