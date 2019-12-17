"""
Secret Sharing
==============

"""

from setuptools import setup
import pyseltongue

setup(
    name='pyseltongue',
    version=pyseltongue.__version__,
    url='https://github.com/ginsburgnm/pyseltongue',
    license='MIT',
    author='nginsburg',
    author_email='ginsburgnm@gmail.com',
    description=("Tools for sharing secrets (like Bitcoin private keys), "
                 "using shamir's secret sharing scheme."),
    packages=[
        'pyseltongue',
    ],
    zip_safe=False,
    install_requires=[
        'six',
        'utilitybelt',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
