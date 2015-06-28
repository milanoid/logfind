try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'lofind',
    'author': 'Milan Vojnovic',
    'url': 'https://github.com/milanoid/logfind',
    'download_url': 'https://github.com/milanoid/logfind',
    'author_email': 'milanvojnovic@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)