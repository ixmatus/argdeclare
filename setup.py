import sys
from distutils.core import setup

version = '0.4.14'

with open("LICENSE", 'r') as f:
    LICENSE = f.read()

setup(name="argdeclare",
      version=version,
      description="Argdeclare is a declarative argument configurator for python's argparse.",
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
      packages=["argdeclare"]
      )
