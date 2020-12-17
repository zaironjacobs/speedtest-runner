from setuptools import setup
from setuptools import find_packages

name = 'speedtest-runner'
version = '0.0.1'

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = [
    'colorama>=0.4.4'
]

setup(
    name=name,
    version=version,
    author='Zairon Jacobs',
    author_email='zaironjacobs@gmail.com',
    description='Run Speedtest in the console',
    long_description=long_description,
    url='',
    download_url='',
    keywords=['speedtest', 'runner'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [name + '=speedtest_runner.app:main'],
    },
    install_requires=requires,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English'
    ],
    python_requires='>=3',
)
