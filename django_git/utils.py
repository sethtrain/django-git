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
    repo_path = os.path.join(settings.REPOS_ROOT, dir)
    return Repo(repo_path)

def get_commit(name, commit):
    repo = get_repo(name)
    commit = repo.commit(commit)
    return commit

def get_blob(repo, commit, file):
    repo = get_repo(repo)
    commit = repo.commit(commit)
    tree = commit.tree
    for path_seg in file.split('/'):
        t = tree.get(path_seg)
        if isinstance(t, Tree):
            tree = t
        else:
            blob = t
    return blob
