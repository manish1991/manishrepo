from django.conf.urls import include, url
from django.contrib import admin

from art.views import home, detail_page

urlpatterns = [
    # Examples:
    # url(r'^$', 'article.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^article/details/(?P<article_id>\d+)/$', detail_page),
    
]
