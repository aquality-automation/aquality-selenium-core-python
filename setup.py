from setuptools import find_packages, setup

with open('requirements.txt') as requirements:
    parse_requirements = requirements.read()

setup(
    install_requires=parse_requirements,
    name='aquality-selenium-core',
    version='0.0.1',
    packages=find_packages(include=['aquality_selenium_core*']),
    url='https://github.com/aquality-automation/aquality-selenium-core-python',
    license='Apache 2.0',
    author='',
    author_email='',
    description=''
)
