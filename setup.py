# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wau',
    version='0.1.0',
    description='Work Automation Utils',
    long_description=readme,
    author='Xiyu Wang',
    author_email='sionwxy@gmail.com',
    url='https://github.com/SionWxy/wau',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'bin'))
)
