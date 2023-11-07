#!/usr/bin/env python

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='itm_schema',
        version='0.0.1',
        url='n/a',
        author='SoarTech',
        author_email='n/a',
        description='In the moment TA1 schema',
        packages=find_packages('src'),    
        package_dir={'': 'src'},
        install_requires=[
            'pydantic',
            'scikit-learn',
            'requests', # for unit tests
        ]
    )

