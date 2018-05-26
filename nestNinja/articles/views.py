from django.shortcuts import render
from.models import Articles
# Create your views here.


def articles_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {"articles": articles})
