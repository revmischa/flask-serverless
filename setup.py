"""
Flask-Serverless
----------------

Easy integration of Flask with AWS Lambdas.
"""
from setuptools import setup

def parse_requirements(filename):
    """load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name='Flask-Serverless',
    version='0.1.0',
    url='https://github.com/revmischa/flask-serverless',
    license='WTFPL',
    author='Mischa Spiegelmock',
    author_email='mischa@mvstg.biz',
    description='AWS Lambda easy integration with Flask web framework.',
    long_description=__doc__,
    packages=['flask_serverless'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
#    test_requires=[
        # 'mock',
        # 'requests'
    # ],
    # test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: WTFPL',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
