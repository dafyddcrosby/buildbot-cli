#!/usr/bin/python
from distutils.core import setup
setup(name='buildbot-cli',
    version='0.1',
    description='Command line buildbot control',
    long_description='Command line buildbot control',
    author='Dafydd Crosby',
    author_email='dafydd@dafyddcrosby.com',
    maintainer='Dafydd Crosby',
    maintainer_email='dafydd@dafyddcrosby.com',
    url='https://github.com/dafyddcrosby/buildbot-cli',
    scripts=["buildbot-cli"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ],
    )
