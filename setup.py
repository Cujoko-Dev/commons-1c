# -*- coding: utf-8 -*-
from __future__ import absolute_import

from setuptools import find_packages, setup

import commons_1c

setup(
    name='commons_1c',
    version=commons_1c.__version__,
    description='Commons for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://gitlab.com/Cujoko/commons-1c',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c commons',
    license='MIT',
    install_requires=[
        'appdirs>=1.4.3',
        'commons @ https://gitlab.com/Cujoko/commons/-/archive/master/commons-master.tar.gz#egg=commons-2.1.0',
        'six>=1.11.0'
    ]
)
