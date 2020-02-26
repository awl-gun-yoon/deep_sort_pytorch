#!/usr/bin/env python

from distutils.core import setup

setup(name='deep_sort_pytorch',
      version='1.0',
      description='Deep sort algorithm written in pytorch',
      author='ZQPei',
      author_email='dfzspzq@163.com',
      url='https://github.com/ZQPei/deep_sort_pytorch',
      packages=['deep_sort_pytorch.deep_sort',
                'deep_sort_pytorch.deep_sort.deep',
                'deep_sort_pytorch.deep_sort.sort'],
      )
