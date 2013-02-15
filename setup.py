#!/usr/bin/env python

from distutils.core import setup

setup(name='snowballstemmer',
      version='1.0.0',
      description='This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms.',
      long_description='''
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish
''',
      author='Yoshiki Shibukawa',
      author_email='yoshiki at shibu.jp',
      url='https://github.com/shibukawa/snowball_py',
      keywords="stemmer",
      license="BSD",
      package_dir={"snowballstemmer": "src/snowballstemmer"},
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Natural Language :: Danish',
          'Natural Language :: Dutch',
          'Natural Language :: English',
          'Natural Language :: Finnish',
          'Natural Language :: French',
          'Natural Language :: German',
          'Natural Language :: Hungarian',
          'Natural Language :: Italian',
          'Natural Language :: Norwegian',
          'Natural Language :: Portuguese',
          'Natural Language :: Romanian',
          'Natural Language :: Russian',
          'Natural Language :: Spanish',
          'Natural Language :: Swedish',
          'Natural Language :: Turkish',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: PyPy'
     ]
)
