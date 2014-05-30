from setuptools import setup, find_packages
import sys

# get around issues importing sqlalchemy
if sys.version_info<(3,0,0):
    execfile('sabridge/version.py')
else:
    fname = 'sabridge/version.py'
    exec(compile(open(fname, "rb").read(), fname, 'exec'))

tests_require = [
    'Django>=1.2,<1.7',
]
setup(
    name='django-sabridge',
    version=__version__,
    author='John Paulett',
    author_email='john@paulett.org',
    url='https://django-sabridge.readthedocs.org',
    description = 'Provides SQLAlchemy access to Django models.',
    license='BSD',
    packages=find_packages(exclude=('tests',)),
    zip_safe=True,
    install_requires=[
        'sqlalchemy>=0.6.0',
    ], 
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Software Development'
    ],
)
