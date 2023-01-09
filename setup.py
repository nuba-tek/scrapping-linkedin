from setuptools import setup
from setuptools import find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='scrapping-linkedin',
    version='0.1.0',
    packages=['linkedin_scraper'],
    url='',
    license=license,
    author='Nuba Tek',
    author_email='',
    description='',
    long_description=readme
)

