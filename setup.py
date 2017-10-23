try:
    from setuptools import setup, find_packages
except ImportError:
    import sys
    sys.stderr.write("Error: setuptools is required to install this package.")
    sys.exit(1)


__version__ = '1.5'
__author__ = 'Alexander Chaika'
__email__ = 'manti.by@gmail.com'
__license__ = 'NEW-BSD'

setup(
    name='django-simple-rest-3',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='A drop dead simple package for creating RESTful APIs on top of Django',
    long_description=open('README.rst').read(),
    url='https://github.com/manti-by/django-simple-rest',
    packages=find_packages(),
    install_requires=['setuptools', 'mimeparse'],
    zip_safe=False,
    keywords='rest,django,api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
