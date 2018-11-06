"""
Flask-Serverless
----------------

Easy integration of Flask with AWS Lambdas.
"""
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

def parse_requirements(filename):
    """load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name='Flask-Serverless',
    version='0.1.2',
    url='https://github.com/revmischa/flask-serverless',
    license='WTFPL',
    author='Mischa Spiegelmock',
    author_email='mischa@mvstg.biz',
    description='AWS Lambda easy integration with Flask web framework.',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        'License :: OSI Approved',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
