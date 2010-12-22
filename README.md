README
======

Get the code via svn:

    git checkout git://github.com/sethtrain/django-git.git

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

Then collect the static files, ensuring AppDirectoriesFinder is in STATICFILES_FINDERS:

    ./manage.py collectstatic -n
    # And if that outputs some js/jquery-1.2.6.min.js file and our js/commit.js, continue
    ./manage.py collectstatic

If there are name resolution issues with commit.js, rename it in templates/django_git/commit.html and move it appropriately.

With the use of [auto_render](http://djangosnippets.org/snippets/559/), using this app in other projects/apps is much simpler. Apps, not wanting to show the repo/commit/blob directly but handle them in their own way, can simply call the view with only_context=True:

    @auto_render
    def some_other_view(request, repo='', commit_id='')
        if not commit_id or not repo: raise Http404

        ctx = django_git.views.commit(request, repo, commit_id, only_context=True)
        diffs = ctx['diffs']
        ...
        # Though a more direct use of django_git.utils could be used if necessary as well:
        diffs = django_git.utils.get_commit(repo,commit).diffs


Requirements

* Pygments
* GitPython
* Django 1.3 (alpha or better)

If you would like to get started with django-git [Hugh Brown](http://github.com/hughdbrown) has created [Django-git-tester](http://github.com/hughdbrown/Django-git-tester).

Thanks!
-------
* Christos Trochalakis
* Hugh Brown
* Fahrzin Hemmati
