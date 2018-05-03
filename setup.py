#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


setup(name='python-ubx',
      version='0.1',
      description='A python library implementing the binary u-blox UBX protocol.',
      author='Sebastian Krämer',
      author_email='basti.kr@gmail.com',
      url='https://github.com/bastikr/python-ubx',
      packages=['ubx', 'ubx.descriptions'],
      scripts=['scripts/ubxstats'],
      install_requires=["bitarray"]
     )
