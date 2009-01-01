#!/usr/bin/env python
from setuptools import setup

setup(
    name='django_git',
    version='0.1',
    description='django gitweb replacement',
    classifiers = [ 'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    author='Seth Buntin',
    author_email='sethtrain@gmail.com',
    url='http://code.google.com/p/django-git',
    packages=['django_git', 'django_git.templatetags'],
    package_data={ 'django_git' : ['templates/django_git/*.html', 'media/js/*.js']},
    zip_safe=False,
    install_requires=['GitPython >=0.1.4', 'Pygments >=0.11'],
)
