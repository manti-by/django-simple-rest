#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    import sys
    sys.stderr.write("Error: setuptools is required to install this package.")
    sys.exit(1)

from djrest import __version__


setup(
    name='djrest',
    version=__version__,
    author='Alexander Chaika',
    author_email='manti.by@gmail.com',
    description='Simple REST library for Django',
    long_description=open('README.md').read(),
    url='https://github.com/manti-by/djrest',
    license='BSD',
    packages=find_packages(),
    install_requires=['setuptools', 'mimeparse'],
    keywords='rest,django,api',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
