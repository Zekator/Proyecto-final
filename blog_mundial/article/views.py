from django.shortcuts import render
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
        template_name="article_list.html"
    )

def article_create(request):
    return render(request, 'article_form.html')



