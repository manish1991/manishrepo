from art.models import Article

def all_common_variables(request):
    """
    setting the variables which can be used in all the views functions.
    """
    articles = Article.objects.all()
    random_article = Article.objects.order_by('?')[0:4]
    return {
            'articles':articles,
            'random_article':random_article,
            }