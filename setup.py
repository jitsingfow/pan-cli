from setuptools import setup, find_packages
from project_info import VERSION

setup(
    name='pan-cli',
    version={VERSION},
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'pan = main:main'
        ]
    }
)
