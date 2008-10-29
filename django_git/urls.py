from django.conf.urls.defaults import *

urlpatterns = []

urlpatterns += patterns('django_git.views',
    url(r'^(?P<repo>[\w_]+)/diff/(?P<commit>[\w\d]+)/$', 'diff', name='django-git-diff'),
    url(r'^(?P<repo>[\w_]+)/$', 'repo', name='django-git-repo'),
    url(r'^$', 'index', name='django-git-index'),
)
