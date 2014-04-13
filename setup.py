from __future__ import print_function

import sys
import os.path
from setuptools import setup, find_packages

single_version = '--single-version-externally-managed'
if single_version in sys.argv:
    print('[pdb++] WARNING: ignoring unsupported option', single_version, file=sys.stderr)
    sys.argv.remove(single_version)

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

setup(
    name='pdb_shell',
    version='0.7.2',
    author='ya790206',
    py_modules=['pdb_shell'],
    url='https://github.com/ya790206/pdb_shell',
    license='BSD',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    description='pdb_shell, add shell mode for pdbpp',
    long_description=long_description,
    keywords='pdb debugger tab color completion',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Topic :: Utilities",
        ],
    install_requires=["fancycompleter>=0.2",
                      "wmctrl",
                      "pygments"],
)
