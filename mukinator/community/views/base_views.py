from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Post
from django.db.models import Q, Count


def index(request):
    # 디폴트는 최신순 정렬
    post_list = Post.objects.order_by('-create_date')  # 최신순으로 기본 정렬
    sort = request.GET.get('sort', '')
    page = request.GET.get('page', 1)  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    # 지역 셀렉트박스
    if sort == 'seoul':
        post_list = Post.objects.filter(region='서울').order_by('-create_date')  # 복수를 가져올 수 있음
    elif sort == 'suwon':
        post_list = Post.objects.filter(region='수원').order_by('-create_date')
    elif sort == 'busan':
        post_list = Post.objects.filter(region='부산').order_by('-create_date')
    elif sort == 'yongin':
        post_list = Post.objects.filter(region='용인').order_by('-create_date')
    elif sort == 'gimhae':
        post_list = Post.objects.filter(region='김해').order_by('-create_date')
    else:
        post_list = Post.objects.order_by('-create_date')
    #검색 기능
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)  # 글쓴이 검색
        ).distinct()
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'page': page, 'sort': sort, 'kw': kw}
    return render(request, 'community/post_list.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'community/post_detail.html', context)