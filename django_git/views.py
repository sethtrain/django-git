from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from django_git.utils import get_repos, get_repo, get_diff

def index(request, template_name='django_git/index.html'):
    return render_to_response(template_name, {'repos': get_repos()}, context_instance=RequestContext(request))

def repo(request, repo, template_name='django_git/repo.html'):
    return render_to_response(template_name, {'repo': get_repo(repo)}, context_instance=RequestContext(request))

def diff(request, repo, commit, template_name='django_git/diff.html'):
    return render_to_response(template_name, {'diffs': get_diff(repo, commit), 'repo': get_repo(repo), 'commit': commit }, context_instance=RequestContext(request))