README
======

Get the code via svn:

    svn checkout http://django-git.googlecode.com/svn/trunk/ django-git

Add the django-git/django_git folder to your PYTHONPATH.

Update your settings.py:

    INSTALLED_APPS = (
        ...
        'django_git'
        ...
    )

    REPOS_ROOT = '/Users/seth/projects/git'

And don't forget to include the urls.py:

    urlpatterns = patterns('',
        ...
        (r'^git/', include('django_git.urls')),
        ...
    )

Last, make sure you include the file located in the media directory in your project media location so that the ajax and javascript calls will work correctly. If you have a better way of doing this I would be glad to hear.

Requirements

* Pygments
* GitPython

If you would like to get started with django-git [Hugh Brown](http://github.com/hughdbrown) has created [Django-git-tester](http://github.com/hughdbrown/Django-git-tester).
