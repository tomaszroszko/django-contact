import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-contact',
    version='0.1',
    packages=['contact',
              'contact.migrations'
              ],
    include_package_data=True,
    license='BSD License',
    description='Store messages from contact-form in database. Managable from backoffice',
    long_description=README,
    url='https://github.com/tomaszroszko/django-contact',
    author='Tomasz Roszko',
    author_email='tomaszroszko@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
