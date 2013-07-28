import sys
from setuptools import setup, find_packages

version = '0.4.10'

with open("LICENSE", 'r') as f:
    LICENSE = f.read()

with open("README.md", 'r') as f:
    README = f.read()

setup(name="argdeclare",
      version=version,
      description="Argdeclare is a declarative argument configurator for python's argparse.",
      long_description=README,
      classifiers=["Intended Audience :: Developers",
                   "License :: OSI Approved :: Python Software Foundation License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      author="Parnell Springmeyer",
      author_email="parnell@ixmat.us",
      url="https://github.com/ixmatus/argdeclare",
      license=LICENSE,
      zip_safe=False,
      packages=find_packages(),
      include_package_data=True
      )
