from django.shortcuts import get_object_or_404, render

from project.apps.cms.models import Article


def page(request, slug):
    article = get_object_or_404(Article, slug=slug)

    return render(request, 'cms/page.html', {
        'article': article,
    })
