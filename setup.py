#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='wirecloud-markdown-github',
    version='1.2',
    author='CoNWeT Lab',
    author_email='wirecloud@conwet.com',
    description='Set of markdown extensions for getting similar behaviour to GFM.',
    url='https://github.com/conwetlab/markdown_github',
    packages=['markdown_github'],
    install_requires=['markdown>=3.0', 'pymdown-extensions'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
