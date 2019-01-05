from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from django.contrib.auth.decorators import login_required
from .import forms


def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)

    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticles(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('articles:list')
    else:
        form = forms.CreateArticles()
    return render(request, 'articles/article_create.html', {'form': form})


def article_update(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    if request.method == 'PUT':
        form = forms.CreateArticles(request.PUT, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.update(commit=False)
            instance.author = request.user
            instance.save()

            return render(request, 'article_update', form)
    else:
        form = forms.CreateArticles()
    return render(request, 'articles/article_update.html', {'form': form})


# def article_delete(request, article):
#     if request.method == 'Delete':
#         form = forms.CreateArticles(request.Delete,)
#         if form.is_valid():
#             # delete article from db
#             instance = form.delete(commit=False)
#             instance.author = request.user
#             instance.delete()
#
#             return redirect('articles:list')
