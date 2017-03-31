import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hub-pip",
    version="0.0.1",
    author="Black Duck Software",
    author_email="",
    description=(
        "Generates and deploy's Black Duck I/O files for use with the Black Duck Hub"),
    license="Apache 2.0",
    keywords="hub-pip blackduck",
    url="https://github.com/blackducksoftware/hub-python-plugin",
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=["configparser", "requests", "six", "docopt"],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
    entry_points={
        'console_scripts': [
            'hub-pip=hub_pip.Main:main',
        ],
    },
)
