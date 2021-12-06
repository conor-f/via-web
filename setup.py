from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIRES = (
    'backoff',
    'packaging',
    'reverse_geocoder',
    'fast_json',
    'boto3',
    'bottle',
    'gunicorn',
    'via-api==0.0.44',
    'osmnx'
)

setup(
    name='via-web',
    version='0.1.11',
    python_requires='>=3.6',
    description='Analysing and serving crowdsourced road quality data',
    author='Conor Flynn',
    url='https://github.com/conor-f/via-web',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'via_bottle = via_web.bin.bottle_entry:main'
        ]
    }
)
