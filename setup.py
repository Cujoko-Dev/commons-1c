# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup

here = Path(__file__).parent

about: Dict[str] = {}
with Path(here, 'commons_1c', '__about__.py').open() as f:
    exec(f.read(), about)

setup(
    name='commons_1c',
    version=about['__version__'],
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
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c commons',
    license='MIT',
    install_requires=[
        'appdirs>=1.4.3',
        'commons @ https://gitlab.com/Cujoko/commons/-/archive/master/commons-master.tar.gz'
    ]
)
