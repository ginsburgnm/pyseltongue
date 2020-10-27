"""
Secret Sharing
==============

"""
from setuptools import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=[
        'pyseltongue',
    ],
    zip_safe=False,
    install_requires=[
        'six',
        'utilitybelt',
    ],
)
