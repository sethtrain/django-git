from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from django_git.utils import *

def index(request, template_name='django_git/index.html'):
    return render_to_response(template_name, {'repos': get_repos()}, context_instance=RequestContext(request))

def repo(request, repo, template_name='django_git/repo.html'):
    return render_to_response(template_name, {'repo': get_repo(repo)}, context_instance=RequestContext(request))

def commit(request, repo, commit, template_name='django_git/commit.html'):
    return render_to_response(template_name, {'diffs': get_commit(repo, commit).diffs, 'repo': get_repo(repo), 'commit': commit }, context_instance=RequestContext(request))

def blob(request, repo, commit):
    file = request.GET.get('file', '')
    blob = get_blob(repo, commit, file)
    lexer = guess_lexer_for_filename(blob.basename, blob.data)
    return HttpResponse(highlight(blob.data, lexer, HtmlFormatter(cssclass="pygment_highlight", linenos='inline')))