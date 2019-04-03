# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

here = Path(__file__).parent

about = {}
with Path(here, 'commons_1c', '__about__.py').open() as f:
    exec(f.read(), about)

setup(
    name='commons-1c',
    version=about['__version__'],
    description='Commons for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://github.com/Cujoko/commons-1c',
    packages=['commons_1c'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c commons',
    license='MIT',
    install_requires=[
        'appdirs>=1.4.3',
        'cjk-commons>=3.3.0'
    ]
)
