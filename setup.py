from setuptools import setup, find_packages

NAME = 'caesar'

setup(
    name=NAME,
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'caesar = caesar.cli:main'
        ]
    }
)