from setuptools import setup


version = '0.5.0'

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='pydict2xml',
    version='0.5.0',
    py_modules=['dict2xml'],
    author=u'Fernando Fl\xf3rez',
    author_email='fernando@funciton.com',
    license='http://opensource.org/licenses/MIT',
    description='Small utility to convert a python dict into an xml tree.',
    long_description=long_description,
    url='https://github.com/fernandoflorez/dict2xml'
)
