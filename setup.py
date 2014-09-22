#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-modernizr3',
    version='.'.join(map(str, __import__('modernizr3').__version__)),
    author='Garet McKinley',
    author_email='garetmckinley@me.com',
    url='https://github.com/mediachicken/django-modernizr3',
    description='Python 3 port of David Gouldin\'s Django Modernizr',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
