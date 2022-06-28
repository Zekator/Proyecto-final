from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from article.models import Article
from user.models import Avatar


def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    articles = Article.objects.all()
    context_dict.update({
        'articles': articles,
                        })
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )
    


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        articles = Article.objects.filter(query)
        context_dict.update({
        'articles': articles,
        'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="article_list.html",
    )

