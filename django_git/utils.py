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
    tree = commit.tree
    for path_seg in file.split('/'):
        if isinstance(tree.get(path_seg), Tree):
            tree = tree.get(path_seg)
        else:
            blob = tree.get(path_seg)
    return blob