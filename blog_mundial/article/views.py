from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from article.forms import ArticleForm

from article.models import Article


# Create your views here.

def article_list(request):
    articles = Article.objects.all()

    context_dict = {
        'articles': articles
    }

    return render(
        request=request,
        context=context_dict,
        template_name="article/article_list.html"
    )

@login_required
def article_form(request):
    if request.method == 'POST':
        articles = Article(request.POST)
        if articles.is_valid():
            data = articles.cleaned_data()
            
            articles = Article(
                name=data['name'],
                description=data['description'],
                country=data['country'],
                article_id=data['article_id'],
                article_content=data['article_content']
                )
            context_dict = {
                'articles': articles              
                }
            
            articles.save()
            return render (request, 'article/article_list.html', context_dict )

        article_form = ArticleForm(request.POST)
        context_dict = {
        'article_form': article_form
            }
        article_form.save()
        return render(
                request=request,
                context=context_dict,
                template_name="article/article_form.html"
            )


def article_detail(request, article_id):
    articles = Article.objects.get(pk=article_id)
    context_dict = {
        'articles': articles
    }
    return render(
        request=request,
        context=context_dict,
        template_name='article/article_detail.html'
    )



