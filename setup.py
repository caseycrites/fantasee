#!/usr/bin/env python

from setuptools import setup

setup(
    name='fantasee',
    version='0.1',
    author='Casey W Crites',
    author_email='crites.casey@gmail.com',
    packages=['fantasee'],
    url='http://pypi.python.org/pypi/fantasee',
    license='LICENSE',
    description='View information about your ESPN fantasy sports leagues.',
    install_requires=[
        'PyYAML>=3.10',
        'beautifulsoup4>=4.2.1',
        'requests>=1.2.3',
        'wsgiref>=0.1.2',
    ],
    entry_points={
        'console_scripts': [
            'fantasee = fantasee.cli:main',
        ]
    },
)
