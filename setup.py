from setuptools import setup

files = ["templates/models_logging/*", "migrations/*", "management/commands/*"]

setup(
    name='Cheetay_Logging',
    version='0.9.7',
    packages=['models_logging'],
    url='https://github.com/BugEncapsulation/Cheetay_logging',
    package_data = {'models_logging' : files},
    license='MIT',
    author='Legion/Ibrahim',
    author_email='muhammad.ibrahim@cheetay.pk',
    description='Add logging of models from save, delete signals',
    keywords=[
        'cheetay logging',
    ],
    install_requires=[
        "django==1.11.15",
        "python-dateutil",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
