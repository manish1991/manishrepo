from django.shortcuts import render
from art.models import Article


def home(request):
    """
    This function is for listing all the article on the listing page.
    """
    return render(request, 'article_listing_page.html', locals())


def detail_page(request, article_id):
    """
    This function is for getting the details of any particular article.
    :param article_id:  This is the selected article id for which we want the detail information.

    """
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail_page.html', locals())