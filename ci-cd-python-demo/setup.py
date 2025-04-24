# setup.py

from setuptools import setup, find_packages

setup(
    name='user_service',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'run-user-service = user_service.main:main'
        ]
    },
)

