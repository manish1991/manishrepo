from django.contrib import admin
from art.models import Article


class AdminArticle(admin.ModelAdmin):
    """
    Registering the Article model in the admin, so that we can create new article with its details.
    """
    list_display = ('title','author','publication','category', 'hero_image', 'optional_image', 'body_text',)
   
admin.site.register(Article, AdminArticle)