import os
from setuptools import setup

README=open(os.path.join(os.path.dirname(__file__),'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))
setup(
    name='django_polls',
    version='0.1',
    packages=['polls'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to conduct web-based polls',
    long_description=README,
    url='http://django.com',
    author='phiree-django',
    author_email='phiree@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Diango',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System::OS Independent',
        'Programing language::Python',
        'Programming Language::Python 3.3',
        'Topic::Internet::WWW/HTTP',
        'Topic::Internet::WWW/HTTP::Dynamic Content'
        ],
    )
