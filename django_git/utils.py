import os
from git import *

from django.conf import settings

def get_repos():
    return [Repo(os.path.join(settings.REPOS_ROOT, dir)) for dir in os.listdir(settings.REPOS_ROOT) if os.path.isdir(os.path.join(settings.REPOS_ROOT, dir))]

def get_repo(name):
    return Repo(os.path.join(settings.REPOS_ROOT, name))

def get_diff(name, commit):
    repo = get_repo(name)
    commit = repo.commit(commit)
    return commit.diffs