# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='ruleset',

        version='1.0.3',

        description='Bayesian Rule Set Mining',
        long_description=long_description,

        url='https://github.com/zli37/bayesianRuleSet',
        author='Zhen Li, Tong Wang',
        author_email='tong-wang@uiowa.edu',

        license='MIT',

        classifiers=[
            # How mature is this project? 
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
        ],

        keywords='data mining analysis',
        packages=find_packages(exclude=['contrib', 'docs', 'tests']),
        install_requires=[
            'pandas',
            'numpy',
            'scipy',
            'sklearn'
        ],
        python_requires='>=3',
)
