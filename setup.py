from setuptools import setup, find_packages

setup(
    name="dogage",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dogage=main:main'
        ]
    }
) 