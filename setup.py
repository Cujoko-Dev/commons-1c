#! python3.6
# -*- coding: utf-8 -*-
from setuptools import setup

import commons_1c

setup(
    name='commons_1c',

    version=commons_1c.__version__,

    description='Commons for 1C:Enterprise',

    url='https://github.com/Cujoko/commons-1c',

    author='Cujoko',
    author_email='cujoko@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Natural Language :: Russian',

        'Programming Language :: Python :: 3.6',

        'Topic :: Software Development',
        'Topic :: Utilities'
    ],

    keywords='1c commons',

    install_requires=[
        'appdirs'
    ],

    py_modules=['commons_1c']
)
