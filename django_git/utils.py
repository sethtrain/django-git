import os
from git import *

from django.conf import settings

def get_repos():
    repos = []
    for dir in os.listdir(settings.REPOS_ROOT):
        if os.path.isdir(os.path.join(settings.REPOS_ROOT, dir)):
            try:
                repos.append(Repo(os.path.join(settings.REPOS_ROOT, dir)))
            except Exception:
                continue
    return repos

def get_repo(name):
    return Repo(os.path.join(settings.REPOS_ROOT, name))

def get_commit(name, commit):
    repo = get_repo(name)
    commit = repo.commit(commit)
    return commit

def get_blob(repo, commit, file):
    repo = get_repo(repo)
    commit = repo.commit(commit)
    file = file.split('/')
    length = len(file)
    tree = commit.tree
    for item in xrange(len(file)):
        if isinstance(tree.get(file[item]), Tree):
            tree = tree.get(file[item])
        else:
            blob = tree.get(file[item])
    return blob