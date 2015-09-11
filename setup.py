from setuptools import setup
#import os.path

long_description = """
The purpose of this sphinx extension is enable markup of requirements per the definitions in RFC 2119.

 * http://sphinx-doc.org
 * https://www.ietf.org/rfc/rfc2119.txt

This is supported by a suite of requirement directives that correspond to the RFC 2119 keywords. There are also a suite of requirement list directives that support documenting reqiurements (that have been defined with the rfc2119 directives).

This module is in ALPHA status. Feedback / pull requests very welcome. Development occurs on GitHub:

 * https://github.com/monkeypants/sphinx.rfc2119/

Documentation is a bit strange - I used the directives to document what it is supposed to do. Which was handy as I made it, but probably not very readable.

Basically, add the module to your the conf.py of your repo then use the directives. They have lower case names.

"""

#localcss = os.path.join(
#    os.path.dirname(os.path.abspath(__file__)),
#    "_static",
#    "css",
#    "rfc2119.css")

setup(
    name='sphinx_rfc2119',
    version='0.0.9',
    description='RFC2119 directives for Sphinx documentation',
    long_description=long_description,
    url='https://github.com/monkeypants/sphinx.rfc2119',
    author='Chris Gough',
    author_email='christopher.d.gough-pypi@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        # only tested with python 2.7
        # other versions likely to work
        'Programming Language :: Python :: 2.7',
    ],
    keywords='RFC2119 directives Sphinx docutils',
    py_modules = ['sphinx_rfc2119'],
    data_files = [
        ('_static/css', ["_static/css/rfc2119.css"]),],
    install_requires=['Sphinx'],
)
