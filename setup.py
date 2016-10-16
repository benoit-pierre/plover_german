#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_german',
    version = '0.1.0',
    description = 'German system for Plover',
    author = 'Foo Bar',
    author_email = 'foo.bar@foobar.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop'
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
    ],
    py_modules = [
        'plover_german',
    ],
    entry_points = '''

    [plover.system]
    German Stenotype = plover_german

    ''',
    zip_safe = True,
)
