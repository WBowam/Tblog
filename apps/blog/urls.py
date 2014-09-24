from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import home, detail, category_articles, tag_articles, like, dislike

urlpatterns = patterns('',
                       # Examples:
                       url(r'^index$', home, name='home'),
                       url(r'^category/(?P<category_name>\w+)/$',
                           category_articles,
                           name='category_articles'
                           ),
                       url(r'^tag/(?P<tag_name>\w+)/$',
                           tag_articles,
                           name='tag_articles'
                           ),
                       url(r'^detail/(?P<id>\d)/$', detail, name='detail'),
                       url(r'^like/(?P<id>\d)/$', like, name='like'),
                       url(r'^dislike/(?P<id>\d)/$', dislike, name='dislike'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       )
