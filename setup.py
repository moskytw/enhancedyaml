from distutils.core import setup

from enhancedyaml import __version__

setup(
    name    = 'enhancedyaml',
    description = 'It makes it more convenient to use PyYAML.',
    long_description = open('README.rst').read(),
    version = __version__,
    author  = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    #url = 'http://enhancedyaml.mosky.tw/',
    url = 'https://github.com/moskytw/enhancedyaml',
    py_modules = ['enhancedyaml'],
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

