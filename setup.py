from setuptools import setup

VERSION = '0.0.1' 
DESCRIPTION = 'Automated labeling'
LONG_DESCRIPTION = 'Automated labeling that takes regexes, keywords, etc.'

REQUIRED_PKGS = [
    'numpy',
    'scipy',
    'sklearn',
    'pandas',
    
]

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="lfuncs", 
        version=VERSION,
        author="Carlos Alas",
        author_email="carlos.alas@sitel.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['lfuncs'],
        install_requires=REQUIRED_PKGS, 
        license='Apache 2.0',
        keywords=['python', 'labeling'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Data Scientists",
            "Programming Language :: Python :: 3",
            
        ]
)