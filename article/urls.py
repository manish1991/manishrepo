from django.conf.urls import include, url
from django.contrib import admin

from art.views import home, detail_page

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),               #Url to login to admin dashboard with admin user credentials.
    url(r'^$', home),                                        #Url of the home page  where all the Articles available are listed.                            
    url(r'^article/details/(?P<article_id>\d+)/$', detail_page), #Url of the Article details page,where we can see Article's details.
    
]
